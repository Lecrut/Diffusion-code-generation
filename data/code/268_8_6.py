class FirstWordExtractor:
    @staticmethod
    def extract_first_word(line):
        return line.split()[0]

    @classmethod
    def read_and_print_first_words(cls, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    first_word = cls.extract_first_word(line)
                    print(first_word)
        except FileNotFoundError:
            print("File not found")

if __name__ == '__main__':
    sample_filename = "sample.txt"
    with open(sample_filename, 'w') as f:
        f.write("This is the first line of the file.\n")
        f.write("This is the second line.")
    FirstWordExtractor.read_and_print_first_words(sample_filename)