def read_and_print_first_word(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():
                    first_word = line.split()[0]
                    print(first_word)
                    break
    except FileNotFoundError:
        print('File not found')
if __name__ == '__main__':
    sample_filename = 'sample.txt'
    with open(sample_filename, 'w') as f:
        f.write('This is the first line of the file.\n')
        f.write('This is the second line.')
    read_and_print_first_word(sample_filename)