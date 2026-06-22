INPUT_FILE = 'sample.txt'
OUTPUT_FILE = 'output_no_spaces.txt'

def remove_spaces(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    cleaned_content = ''.join(content.split())
    with open(output_file, 'w') as file:
        file.write(cleaned_content)

if __name__ == '__main__':
    remove_spaces(INPUT_FILE, OUTPUT_FILE)