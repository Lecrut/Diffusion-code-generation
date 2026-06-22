class SpaceRemover:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_content(self):
        with open(self.input_file, 'r') as file:
            return file.read()

    def write_content(self, content):
        with open(self.output_file, 'w') as file:
            file.write(content)

    def remove_spaces(self):
        content = self.read_content()
        cleaned_content = ''.join(content.split())
        self.write_content(cleaned_content)

if __name__ == '__main__':
    remover = SpaceRemover('sample.txt', 'output.txt')
    remover.remove_spaces()
    print("Spaces removed and written to output.txt")