import os
def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as f:
            items = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{input_filename}': {e}")
        return None
    if not items:
        print("Input file is empty.")
        return []
    print("Available items:")
    for i, item in enumerate(items):
        print(f"{i + 1}: {item}")
    try:
        item_to_remove_input = input("Enter the number of the item to remove: ")
        if not item_to_remove_input.isdigit():
            print("Invalid input. Operation cancelled.")
            return items
        index_to_remove = int(item_to_remove_input) - 1
        if 0 <= index_to_remove < len(items):
            updated_items = items[:index_to_remove] + items[index_to_remove+1:]
            with open(output_filename, 'w') as f:
                for item in updated_items:
                    f.write(item + '\n')
            print(f"Successfully removed item at index {index_to_remove}.")
            print(f"Updated list written to '{output_filename}'.")
            return updated_items
        else:
            print("Invalid item number specified.")
            return items
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return items
    except IOError as e:
        print(f"Error writing to output file '{output_filename}': {e}")
        return items
if __name__ == '__main__':
    INPUT_FILE = "input.txt"
    OUTPUT_FILE = "output.txt"
    sample_data = ["apple", "banana", "cherry", "date", "elderberry"]
    try:
        with open(INPUT_FILE, 'w') as f:
            for item in sample_data:
                f.write(item + '\n')
        print(f"Created sample input file: {INPUT_FILE}")
        items = sample_data
        if len(items) > 1:
            index_to_remove = 1
            updated_items = items[:index_to_remove] + items[index_to_remove+1:]
            with open(OUTPUT_FILE, 'w') as f:
                for item in updated_items:
                    f.write(item + '\n')
            print(f"Simulated removal of item at index {index_to_remove}.")
            print(f"Updated list written to '{OUTPUT_FILE}'.")
    except IOError as e:
        print(f"An error occurred during file setup: {e}")