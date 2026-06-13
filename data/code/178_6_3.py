def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile:
        for line in infile:
            words = line.split()
            with open(output_filename, 'w') as outfile:
                for word in words:
                    outfile.write(word + '\n')
if __name__ == '__main__':
    input_file = "input.txt"
    output_file = "output.txt"
    with open(input_file, 'w') as f:
        f.write("This is the first line.\n")
        f.write("Second line with more words.\n")
        f.write("And a final line.")
    process_file(input_file, output_file)