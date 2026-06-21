import os

def group_files_by_extension(file_paths):
    grouped_files = {}
    for path in file_paths:
        _, ext = os.path.splitext(path)
        if ext not in grouped_files:
            grouped_files[ext] = []
        grouped_files[ext].append(path)
    return grouped_files

if __name__ == '__main__':
    sample_paths = [
        "document.txt",
        "image.jpg",
        "presentation.pptx",
        "report.docx",
        "photo.jpg"
    ]
    result = group_files_by_extension(sample_paths)
    print(result)