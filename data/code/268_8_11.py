def get_first_word(filename):
    with open(filename, 'r') as file:
        return [line.split()[0] for line in file if line.strip()]

if __name__ == '__main__':
    sample_filename = 'sample.txt'
    print(get_first_word(sample_filename))