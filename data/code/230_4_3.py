def check_filenames(filenames):
    for filename in filenames:
        if filename.endswith('.txt'):
            print(filename)
if __name__ == '__main__':
    sample_filenames = [
        "file1.txt",
        "document.doc",
        "image.jpg",
        "report.txt",
        "data.csv",
        "notes.txt"
    ]
    check_filenames(sample_filenames)