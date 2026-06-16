def read_and_print_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as f1:
            content1 = f1.read()
            print("--- Content of File 1 ---")
            print(content1)
            print("\n--- Content of File 2 ---")
            with open(file2_path, 'r') as f2:
                content2 = f2.read()
                print(content2)
    except FileNotFoundError as e:
        print(f"Error: One of the files was not found: {e}")
if __name__ == '__main__':
    file1_name = "file1.txt"
    file2_name = "file2.txt"
    with open(file1_name, 'w') as f:
        f.write("This is the content of the first file.\nLine two.")
    with open(file2_name, 'w') as f:
        f.write("This is the content of the second file.\nAnother line here.")
    read_and_print_files(file1_name, file2_name)