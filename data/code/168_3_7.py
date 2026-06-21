import os

def group_files_by_extension(file_paths):
    categorized_files = {}
    for path in file_paths:
        _, ext = os.path.splitext(path)
        if ext not in categorized_files:
            categorized_files[ext] = []
        categorized_files[ext].append(path)
    return categorized_files

if __name__ == '__main__':
    sample_paths = [
        "file1.txt",
        "image.png",
        "document.pdf",
        "backup.tar.gz",
        "script.py"
    ]
    result = group_files_by_extension(sample_paths)
    print(result)