def reverse_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if not all(isinstance(line, str) for line in lines):
        raise ValueError("All elements in the file must be strings")
    reversed_lines = lines[::-1]
    return ''.join(reversed_lines)

if __name__ == '__main__':
    sample_text = "Line 1\nLine 2\nLine 3"
    with open('sample.txt', 'w') as file:
        file.write(sample_text)
    result = reverse_lines('sample.txt')
    print(result)