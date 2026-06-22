def first_word_from_line(line):
    words = line.split()
    if words:
        return words[0]
    else:
        return ""

def read_and_print_first_words(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(first_word_from_line(line.strip()))
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")

if __name__ == '__main__':
    sample_filename = "sample.txt"
    with open(sample_filename, 'w') as f:
        f.write("This is the first line of the file.\n")
        f.write("This is the second line.")
    read_and_print_first_words(sample_filename)