def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
        output_list = []
        for line in lines:
            output_list.append(line.strip())
        with open(output_filename, 'w') as outfile:
            for item in output_list:
                outfile.write(item + '\n')
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
if __name__ == '__main__':
    INPUT_FILE = 'input.txt'
    OUTPUT_FILE = 'output.txt'
    sample_data = [
        "apple\n",
        "banana\n",
        "cherry\n",
        "date\n"
    ]
    with open(INPUT_FILE, 'w') as f:
        f.writelines(sample_data)
    process_file(INPUT_FILE, OUTPUT_FILE)