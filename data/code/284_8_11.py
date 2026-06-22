def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def reverse_lines(lines):
    return lines[::-1]

def write_lines_to_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

if __name__ == '__main__':
    input_file = 'sample.txt'
    output_file = 'reversed_sample.txt'

    sample_text = "Line 1\nLine 2\nLine 3"
    with open(input_file, 'w') as file:
        file.write(sample_text)

    lines = read_file_lines(input_file)
    reversed_lines = reverse_lines(lines)
    write_lines_to_file(output_file, reversed_lines)

    print("Reversed content written to", output_file)