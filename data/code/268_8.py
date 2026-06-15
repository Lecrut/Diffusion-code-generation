def read_and_print_first_word(filename):
    try:
        with open(filename, 'r') as file:
            first_line = file.readline()
            if first_line:
                first_word = first_line.split()[0]
                print(first_word)
            else:
                print("")
    except FileNotFoundError:
        print("File not found")
if __name__ == '__main__':
    sample_filename = "sample.txt"
    with open(sample_filename, 'w') as f:
        f.write("This is the first line of the file.\n")
        f.write("This is the second line.")
    read_and_print_first_word(sample_filename)