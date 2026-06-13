def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            words = line.split()
            outfile.write('\n'.join(words) + '\n')
if __name__ == '__main__':
    input_file = "input.txt"
    output_file = "output.txt"
    with open(input_file, 'w') as f:
        f.write("This is a sample line.\n")
        f.write("Another line with more words.\n")
        f.write("Single word test.")
    process_file(input_file, output_file)