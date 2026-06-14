def check_filenames():
    filenames = [
        "file1.txt",
        "document.doc",
        "image.jpg",
        "report.txt",
        "data.csv",
        "notes.txt"
    ]
    for filename in filenames:
        if filename.endswith(".txt"):
            print(filename)
if __name__ == '__main__':
    check_filenames()