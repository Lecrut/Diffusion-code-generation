import os
def process_file(input_filename, output_filename, item_to_remove):
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Error: Input file {input_filename} not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return
    modified_lines = []
    for line in lines:
        if line.strip() != item_to_remove:
            modified_lines.append(line)
    try:
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)
        print(f"Successfully removed '{item_to_remove}' and wrote results to {output_filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
if __name__ == '__main__':
    INPUT_FILE = "input.txt"
    OUTPUT_FILE = "output.txt"
    ITEM_TO_REMOVE = "REMOVE_ME"
    sample_data = [
        "Apple\n",
        "Banana\n",
        "REMOVE_ME\n",
        "Cherry\n",
        "Date\n"
    ]
    with open(INPUT_FILE, 'w') as f:
        f.writelines(sample_data)
    process_file(INPUT_FILE, OUTPUT_FILE, ITEM_TO_REMOVE)
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r') as f:
            print("\nContent of output file:")
            print(f.read())