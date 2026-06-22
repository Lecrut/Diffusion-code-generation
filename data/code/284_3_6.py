class IntegerReverser:
    def __init__(self, file_path):
        self.file_path = file_path

    def reverse_integers_in_file(self):
        with open(self.file_path, 'r') as file:
            integers = [int(line.strip()) for line in file]
        reversed_integers = list(reversed(integers))
        with open(self.file_path, 'w') as file:
            for number in reversed_integers:
                file.write(f"{number}\n")

if __name__ == '__main__':
    reverser = IntegerReverser('sample.txt')
    with open('sample.txt', 'w') as file:
        file.write("1\n2\n3\n4\n5\n")
    reverser.reverse_integers_in_file()
    with open('sample.txt', 'r') as file:
        print(file.read())