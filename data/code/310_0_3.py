def read_and_print_files():
    file1_path = "file1.txt"
    file2_path = "file2.txt"
    try:
        with open(file1_path, 'r') as f1:
            content1 = f1.read()
            print("--- Content of", file1_path, "---")
            print(content1)
        with open(file2_path, 'r') as f2:
            content2 = f2.read()
            print("--- Content of", file2_path, "---")
            print(content2)
    except FileNotFoundError as e:
        print(f"Error: One of the required files was not found: {e}")
if __name__ == '__main__':
    with open("file1.txt", "w") as f:
        f.write("This is the content of the first file.\nLine two.")
    with open("file2.txt", "w") as f:
        f.write("This is the content of the second file.\nAnother line here.")
    read_and_print_files()