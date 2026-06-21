import os

class FileCategorizer:
    def __init__(self):
        self.categories = {}

    def add_file(self, file_path):
        _, ext = os.path.splitext(file_path)
        if ext not in self.categories:
            self.categories[ext] = []
        self.categories[ext].append(file_path)

    def get_categories(self):
        return self.categories

if __name__ == '__main__':
    categorizer = FileCategorizer()
    sample_files = [
        "document.pdf",
        "image.png",
        "report.docx",
        "photo.jpg"
    ]
    for file in sample_files:
        categorizer.add_file(file)
    print(categorizer.get_categories())