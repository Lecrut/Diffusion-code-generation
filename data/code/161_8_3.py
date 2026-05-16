def process_file_io(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
        with open(output_filename, 'w') as outfile:
            outfile.writelines(lines)
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except IOError as e:
        print(f"An error occurred during file I/O: {e}")
if __name__ == '__main__':
    input_data = [
        "apple\n",
        "banana\n",
        "cherry\n",
        "date\n"
    ]
    input_file = "input.txt"
    output_file = "output.txt"
    try:
        with open(input_file, 'w') as f:
            f.writelines(input_data)
        process_file_io(input_file, output_file)
    except IOError as e:
        print(f"Error writing sample input file: {e}")