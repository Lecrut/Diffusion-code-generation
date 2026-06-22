def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def reverse_lines(lines):
    return lines[::-1]

def write_lines_to_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)
if __name__ == '__main__':
    sample_text = 'Line 1\nLine 2\nLine 3'
    temp_file_path = 'temp.txt'
    write_lines_to_file(temp_file_path, sample_text.split('\n'))
    lines = read_lines_from_file(temp_file_path)
    reversed_lines = reverse_lines(lines)
    write_lines_to_file(temp_file_path, reversed_lines)
    with open(temp_file_path, 'r') as file:
        result = file.read()
    print(result)