import os

class FileCategorizer:
    def __init__(self):
        self.categories = {}

    def group_by_extension(self, file_paths):
        for path in file_paths:
            _, ext = os.path.splitext(path)
            if ext not in self.categories:
                self.categories[ext] = []
            self.categories[ext].append(path)

    def get_categories(self):
        return self.categories

if __name__ == '__main__':
    categorizer = FileCategorizer()
    sample_paths = [
        "document.txt",
        "image.png",
        "report.pdf",
        "archive.zip",
        "script.py"
    ]
    categorizer.group_by_extension(sample_paths)
    print(categorizer.get_categories())