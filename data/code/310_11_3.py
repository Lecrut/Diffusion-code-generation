import os
class DualPrinter:
    def print_two_files(self, file1_path, file2_path):
        try:
            with open(file1_path, 'r') as f1:
                print("--- Content of File 1 ---")
                print(f1.read())
                print("------------------------\n")
            with open(file2_path, 'r') as f2:
                print("--- Content of File 2 ---")
                print(f2.read())
                print("------------------------")
        except FileNotFoundError as e:
            print(f"Error: One of the files was not found: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    file1_name = "sample_file1.txt"
    file2_name = "sample_file2.txt"
    with open(file1_name, 'w') as f:
        f.write("This is the content of the first file.\nLine two here.")
    with open(file2_name, 'w') as f:
        f.write("This is the content of the second file.\nAnother line for printing.")
    printer = DualPrinter()
    printer.print_two_files(file1_name, file2_name)
    try:
        os.remove(file1_name)
        os.remove(file2_name)
    except OSError:
        pass