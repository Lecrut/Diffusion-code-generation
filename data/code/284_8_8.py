def reverse_lines_in_file(input_path):
    with open(input_path, 'r') as file:
        lines = file.readlines()
    reversed_lines = lines[::-1]
    return ''.join(reversed_lines)

if __name__ == '__main__':
    sample_text = "Hello\nWorld\nThis is a test."
    with open('sample.txt', 'w') as file:
        file.write(sample_text)
    result = reverse_lines_in_file('sample.txt')
    print(result)