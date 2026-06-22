class FileReverser:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_integers(self):
        with open(self.file_path, 'r') as file:
            return [int(line.strip()) for line in file]

    def write_integers_reversed(self):
        integers = self.read_integers()
        with open(self.file_path, 'w') as file:
            for number in reversed(integers):
                file.write(f"{number}\n")

if __name__ == '__main__':
    reverser = FileReverser('sample.txt')
    sample_values = [1, 2, 3, 4, 5]
    with open(reverser.file_path, 'w') as file:
        for value in sample_values:
            file.write(f"{value}\n")
    reverser.write_integers_reversed()
    with open(reverser.file_path, 'r') as file:
        print(file.read())