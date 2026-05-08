import os
def process_list_file(input_filename, output_filename, item_to_remove):
    try:
        with open(input_filename, 'r') as infile:
            items = [line.strip() for line in infile if line.strip()]
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return
    except IOError as e:
        print(f"Error reading file '{input_filename}': {e}")
        return
    if item_to_remove in items:
        updated_items = [item for item in items if item != item_to_remove]
    else:
        updated_items = items
    try:
        with open(output_filename, 'w') as outfile:
            for item in updated_items:
                outfile.write(item + '\n')
        print(f"Successfully updated list. Results written to '{output_filename}'.")
    except IOError as e:
        print(f"Error writing to file '{output_filename}': {e}")
if __name__ == '__main__':
    INPUT_FILE = "input_list.txt"
    OUTPUT_FILE = "output_list.txt"
    ITEM_TO_REMOVE = "remove_me"
    sample_data = [
        "apple",
        "banana",
        "cherry",
        "date",
        "remove_me",
        "elderberry"
    ]
    try:
        with open(INPUT_FILE, 'w') as f:
            for item in sample_data:
                f.write(item + '\n')
        process_list_file(INPUT_FILE, OUTPUT_FILE, ITEM_TO_REMOVE)
    except IOError as e:
        print(f"Error setting up sample input file: {e}")