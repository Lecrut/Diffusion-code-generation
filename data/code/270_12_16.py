def remove_spaces(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    content_no_spaces = content.replace(' ', '')
    with open(output_file, 'w') as file:
        file.write(content_no_spaces)

if __name__ == '__main__':
    remove_spaces('sample.txt', 'output.txt')