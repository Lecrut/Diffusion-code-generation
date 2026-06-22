def first_word_per_line(file_path):
    with open(file_path, 'r') as file:
        return [line.split()[0] for line in file if line.strip()]

if __name__ == '__main__':
    sample_file = 'sample.txt'
    print(first_word_per_line(sample_file))