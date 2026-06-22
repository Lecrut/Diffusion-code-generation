def remove_spaces(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    cleaned_content = ''.join(content.split())
    with open(output_file, 'w') as file:
        file.write(cleaned_content)

if __name__ == '__main__':
    input_path = 'sample_text.txt'
    output_path = 'no_spaces_output.txt'
    remove_spaces(input_path, output_path)