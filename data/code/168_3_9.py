import os.path

def validate_file_paths(file_paths):
    if not all(isinstance(path, str) for path in file_paths):
        raise ValueError("All elements in file_paths must be strings")

def group_by_extension(file_paths):
    validate_file_paths(file_paths)
    categories = {}
    for path in file_paths:
        _, ext = os.path.splitext(path)
        if ext not in categories:
            categories[ext] = []
        categories[ext].append(path)
    return categories

if __name__ == '__main__':
    sample_list = [
        "example.txt",
        "test.pdf",
        "report.docx",
        "image.png",
        "script.py"
    ]
    result = group_by_extension(sample_list)
    print(result)