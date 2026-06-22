class FileReverser:
    @staticmethod
    def read_integers_from_file(file_path):
        with open(file_path, 'r') as file:
            return [int(line.strip()) for line in file]

    @staticmethod
    def write_integers_to_file(file_path, integers):
        with open(file_path, 'w') as file:
            for number in reversed(integers):
                file.write(f"{number}\n")

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    FileReverser.write_integers_to_file(sample_file_path, [1, 2, 3, 4, 5])
    reversed_integers = FileReverser.read_integers_from_file(sample_file_path)
    print(reversed_integers)