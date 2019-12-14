import os
import shutil
from PIL import Image
from datetime import datetime

class PhotOrganizer:

    extensions = ['jpg','jpeg','JGP','JPEG','png','PNG','GIF','gif']

    def create_folder_from_date(self, file):
        date = self.get_shooting_date(file)
        return date.strftime('%Y') + '/' + date.strftime('Y-%m-%d')
        

    def get_shooting_date(self, file):
        photo = Image.open(file)
        info = photo._getexif()
        if 36867 in info:
            date = info[36867]
            date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
            return date
        
        return datetime.fromtimestamp(os.path.getmtime(file))    

    def move_photo(self,file):
        new_folder = self.create_folder_from_date(file)

        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        shutil.move(file, new_folder + '/' + file)

    def organize(self):
        photos = [
            file_name for file_name in os.listdir('.') if any(file_name.endswith(ext) for ext in self.extensions)
        ]
        for file_name in photos:
            self.move_photo(file_name)

PO = PhotOrganizer()
PO.organize()