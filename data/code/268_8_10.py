class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read_and_print_first_word(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    words = line.split()
                    if words:
                        print(words[0])
        except FileNotFoundError:
            print("File not found")

if __name__ == '__main__':
    sample_filename = "sample.txt"
    processor = FileProcessor(sample_filename)
    with open(sample_filename, 'w') as f:
        f.write("This is the first line of the file.\n")
        f.write("This is the second line.")
    processor.read_and_print_first_word()