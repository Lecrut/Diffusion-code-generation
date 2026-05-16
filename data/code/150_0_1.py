import os
def process_file(input_filename, output_filename, item_to_remove):
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
        items = [line.strip() for line in lines if line.strip()]
        if item_to_remove in items:
            modified_items = [item for item in items if item != item_to_remove]
        else:
            modified_items = items
        with open(output_filename, 'w') as outfile:
            for item in modified_items:
                outfile.write(item + '\n')
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
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
    success = process_file(INPUT_FILE, OUTPUT_FILE, ITEM_TO_REMOVE)
    if success:
        print(f"Successfully processed {INPUT_FILE}. Result written to {OUTPUT_FILE}.")
        with open(OUTPUT_FILE, 'r') as f:
            print("\nContent of output file:")
            print(f.read())
    else:
        print(f"Error processing files.")