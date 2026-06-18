import os

def read_and_sort_integers(file_path: str) -> list[int]:
    """Read integers from a file, sort them, and write back to a new file."""
    sorted_list = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
            if not content:
                raise ValueError("The input file is empty.")
                
            # Split the line by spaces and convert each part to an integer
            parts = content.split()
            for item in parts:
                try:
                    num = int(item)
                    sorted_list.append(num)
                except ValueError as e:
                    raise ValueError(f"Invalid integer format found in file at '{item}': {e}") from e
                    
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read/write file(s).")
        exit(1)
    
    # Sort the list of integers in ascending order
    sorted_list.sort()

    output_file = f"{file_path}.sorted"
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(" ".join(map(str, sorted_list))) + "\n"
        
        print(f"Successfully saved {len(sorted_list)} integers to '{output_file}'.")
        
    except PermissionError:
        print(f"Error: Permission denied when writing to output file.")
        exit(1)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or pre-existing files.
    # The script reads from a temporary string-based content simulation if we strictly followed 
    # the "no pre-existing files" rule by creating one on the fly, but to ensure it runs 
    # immediately as requested with hard-coded logic:
    
    sample_data_str = "5 2 8 1 9 3 7"

    # Since the task requires reading a file and we cannot rely on pre-existing files,
    # this script creates a temporary input file in memory simulation by writing to disk 
    # temporarily or simply uses a hardcoded path that it generates. However, to strictly adhere 
    # to "no user input... or pre-existing files", the most robust approach for a runnable module 
    # without an actual physical file present at startup is to create one dynamically if not found,
    # but the prompt says "reads a file". Let's assume we can create it first.

    temp_input_file = "/tmp/input_numbers.txt"
    
    # Create input file with sample data since no pre-existing files are allowed by default state
    try:
        with open(temp_input_file, 'w', encoding='utf-8') as f:
            f.write(sample_data_str + "\n")
        
        read_and_sort_integers(temp_input_file)
    except Exception as e:
        print(f"An unexpected error occurred during file operations: {e}")