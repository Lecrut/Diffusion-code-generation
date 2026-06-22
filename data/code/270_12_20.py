def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def remove_spaces(content):
    return content.replace(' ', '')

def write_file_content(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == '__main__':
    input_path = 'sample.txt'
    output_path = 'output_no_spaces.txt'

    content = read_file_content(input_path)
    cleaned_content = remove_spaces(content)
    write_file_content(output_path, cleaned_content)

    print(f"Spaces removed and saved to {output_path}")