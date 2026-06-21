import os

def group_files_by_extension(file_paths):
    grouped_files = {}
    for file_path in file_paths:
        _, ext = os.path.splitext(file_path)
        if ext not in grouped_files:
            grouped_files[ext] = []
        grouped_files[ext].append(file_path)
    return grouped_files

if __name__ == '__main__':
    sample_file_paths = [
        'document.txt',
        'image.png',
        'report.pdf',
        'photo.jpg',
        'summary.docx'
    ]
    print(group_files_by_extension(sample_file_paths))