import os

def group_files_by_extension(file_paths):
    grouped_files = {}
    for file_path in file_paths:
        _, extension = os.path.splitext(file_path)
        if extension not in grouped_files:
            grouped_files[extension] = []
        grouped_files[extension].append(file_path)
    return grouped_files

if __name__ == '__main__':
    sample_file_paths = [
        'document.pdf',
        'image.png',
        'report.docx',
        'photo.jpg',
        'summary.txt'
    ]
    print(group_files_by_extension(sample_file_paths))