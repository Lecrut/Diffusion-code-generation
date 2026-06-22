def reverse_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    reversed_lines = lines[::-1]
    with open(file_path, 'w') as file:
        file.writelines(reversed_lines)

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    reverse_lines(sample_file_path)