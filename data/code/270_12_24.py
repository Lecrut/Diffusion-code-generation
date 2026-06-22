def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def remove_spaces(input_file, output_file):
    content = read_file(input_file)
    cleaned_content = ''.join(content.split())
    write_file(output_file, cleaned_content)

if __name__ == '__main__':
    input_path = 'sample.txt'
    output_path = 'no_spaces.txt'
    remove_spaces(input_path, output_path)