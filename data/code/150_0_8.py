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
    removed = False
    for line in lines:
        if line.strip() == item_to_remove:
            removed = True
            continue
        modified_lines.append(line)
    with open(output_filename, 'w') as outfile:
        for line in modified_lines:
            outfile.write(line)
    if removed:
        print(f"Successfully removed '{item_to_remove}' and wrote results to {output_filename}")
    else:
        print(f"'{item_to_remove}' was not found in the file. Wrote original content to {output_filename}")
if __name__ == '__main__':
    INPUT_FILE = "input.txt"
    OUTPUT_FILE = "output.txt"
    ITEM_TO_REMOVE = "REMOVE_ME"
    sample_content = [
        "Apple\n",
        "Banana\n",
        "REMOVE_ME\n",
        "Cherry\n",
        "Date\n"
    ]
    with open(INPUT_FILE, 'w') as f:
        f.writelines(sample_content)
    process_file(INPUT_FILE, OUTPUT_FILE, ITEM_TO_REMOVE)
    print("\n--- Verification ---")
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r') as f:
            print(f.read())