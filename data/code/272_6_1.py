import os
def sort_and_write(input_filename, output_filename):
    with open(input_filename, 'r') as infile:
        words = infile.readlines()
    sorted_words = sorted([word.strip() for word in words if word.strip()])
    with open(output_filename, 'w') as outfile:
        for word in sorted_words:
            outfile.write(word + '\n')
if __name__ == '__main__':
    input_file = "input.txt"
    output_file = "output.txt"
    with open(input_file, 'w') as f:
        f.write("zebra\n")
        f.write("apple\n")
        f.write("banana\n")
        f.write("cat\n")
        f.write("dog\n")
    sort_and_write(input_file, output_file)
    with open(output_file, 'r') as f:
        print(f.read())