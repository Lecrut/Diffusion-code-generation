class SpaceRemover:
    INPUT_FILE = 'sample.txt'
    OUTPUT_FILE = 'output_no_spaces.txt'

    @staticmethod
    def remove_spaces(input_file, output_file):
        with open(input_file, 'r') as file:
            content = file.read()
        cleaned_content = ''.join(content.split())
        with open(output_file, 'w') as file:
            file.write(cleaned_content)

if __name__ == '__main__':
    SpaceRemover.remove_spaces(SpaceRemover.INPUT_FILE, SpaceRemover.OUTPUT_FILE)