def reverse_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    reversed_lines = lines[::-1]
    return ''.join(reversed_lines)

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    print(reverse_lines(sample_file_path))