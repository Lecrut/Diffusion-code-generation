import os

def group_files_by_extension(file_paths):
    file_dict = {}
    for path in file_paths:
        _, ext = os.path.splitext(path)
        if ext not in file_dict:
            file_dict[ext] = []
        file_dict[ext].append(path)
    return file_dict

if __name__ == '__main__':
    sample_files = [
        "document.txt",
        "image.png",
        "report.docx",
        "photo.jpg",
        "notes.txt"
    ]
    grouped_files = group_files_by_extension(sample_files)
    print(grouped_files)