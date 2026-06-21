import os
FILE_EXTENSIONS = {'txt': [], 'jpg': [], 'png': [], 'pdf': []}

def group_files_by_extension(file_paths):
    for path in file_paths:
        _, ext = os.path.splitext(path)
        ext = ext[1:].lower()
        if ext in FILE_EXTENSIONS:
            FILE_EXTENSIONS[ext].append(path)
if __name__ == '__main__':
    sample_files = ['document.txt', 'image.jpg', 'photo.png', 'report.pdf', 'notes.txt']
    group_files_by_extension(sample_files)
    print(FILE_EXTENSIONS)