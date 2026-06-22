class FileProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def process(self):
        with open(self.input_file, 'r') as file:
            content = file.read()
        cleaned_content = ''.join(content.split())
        with open(self.output_file, 'w') as file:
            file.write(cleaned_content)

if __name__ == '__main__':
    processor = FileProcessor('sample.txt', 'output_no_spaces.txt')
    processor.process()
    print("Spaces removed and content written to output_no_spaces.txt")