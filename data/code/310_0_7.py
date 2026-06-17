def read_and_print_files():
    file1_path = "file1.txt"
    file2_path = "file2.txt"
    with open(file1_path, 'r') as f1:
        content1 = f1.read()
        print("--- Content of", file1_path, "---")
        print(content1)
        print("\n" + "="*30 + "\n")
    with open(file2_path, 'r') as f2:
        content2 = f2.read()
        print("--- Content of", file2_path, "---")
        print(content2)
if __name__ == '__main__':
    with open("file1.txt", "w") as f:
        f.write("This is the content of the first file.\nIt has multiple lines.")
    with open("file2.txt", "w") as f:
        f.write("This is the content of the second file.\nSequential reading demonstration.")
    read_and_print_files()