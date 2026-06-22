class FileReverser:
    def __init__(self):
        self.file_path = None

    def set_file_path(self, path):
        self.file_path = path

    def reverse_lines(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        reversed_lines = lines[::-1]
        return ''.join(reversed_lines)

if __name__ == '__main__':
    reverser = FileReverser()
    sample_text = "Line 1\nLine 2\nLine 3"
    with open('sample.txt', 'w') as file:
        file.write(sample_text)
    reverser.set_file_path('sample.txt')
    result = reverser.reverse_lines()
    print(result)