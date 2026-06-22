def strip_spaces(source, destination):
    with open(source, 'r') as file:
        data = file.read()
    modified_data = ''.join(data.split())
    with open(destination, 'w') as file:
        file.write(modified_data)

if __name__ == '__main__':
    source_path = 'sample_text.txt'
    destination_path = 'no_spaces_result.txt'
    strip_spaces(source_path, destination_path)