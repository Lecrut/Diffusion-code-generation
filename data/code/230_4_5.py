def check_txt_files():
    filenames = [
        "file1.txt",
        "document.pdf",
        "image.jpg",
        "report.txt",
        "data.csv",
        "notes.txt"
    ]
    for filename in filenames:
        if filename.endswith(".txt"):
            print(filename)
if __name__ == '__main__':
    check_txt_files()