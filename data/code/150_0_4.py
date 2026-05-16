def process_list_file(input_filename, output_filename, item_to_remove):
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
            items = [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print(f"Error: Input file {input_filename} not found.")
        return
    except Exception as e:
        print(f"An error occurred during reading: {e}")
        return
    modified_items = [item for item in items if item != item_to_remove]
    try:
        with open(output_filename, 'w') as outfile:
            for item in modified_items:
                outfile.write(item + '\n')
        print(f"Successfully removed '{item_to_remove}' and wrote the result to {output_filename}")
    except Exception as e:
        print(f"An error occurred during writing: {e}")
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
    process_list_file(INPUT_FILE, OUTPUT_FILE, ITEM_TO_REMOVE)