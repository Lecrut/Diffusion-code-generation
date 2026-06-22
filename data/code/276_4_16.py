class FileRepeater:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_lines(self):
        with open(self.input_file, 'r') as file:
            return file.readlines()

    def write_lines(self, lines, q):
        with open(self.output_file, 'w') as file:
            for line in lines * q:
                file.write(line)

    def repeat_lines(self, q):
        lines = self.read_lines()
        self.write_lines(lines, q)

if __name__ == '__main__':
    repeater = FileRepeater('sample_input.txt', 'output.txt')
    repeater.repeat_lines(3)