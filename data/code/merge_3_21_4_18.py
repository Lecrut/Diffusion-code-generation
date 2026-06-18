import os

def read_and_sort_integers(file_path: str) -> list[int]:
    """Read a single line of space-separated integers from a file, sort them, and return as a list."""
    
    # Check if input file exists to prevent FileNotFoundError for missing files in testing scenarios where the file doesn't exist yet.
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The specified input file '{file_path}' does not exist.")

    try:
        with open(file_path, 'r') as f_in:
            content = f_in.read().strip()
            
            # Handle empty files or lines without integers gracefully by returning an empty list.
            if not content:
                return []
            
            # Split the line and convert parts to integers
            try:
                numbers = [int(num) for num in content.split()]
            except ValueError as e:
                raise ValueError(f"Invalid integer format found in file '{file_path}': {e}") from e
            
    except IOError as e:
        raise RuntimeError(f"Error reading input file '{file_path}': {e}") from e
    
    return sorted(numbers)

def write_sorted_integers(data_list: list[int], output_file_path: str, mode: str = 'w') -> None:
    """Write the sorted integers to a new or existing file."""
    
    try:
        with open(output_file_path, mode + 't', encoding='utf-8') as f_out:
            # Join numbers back into space-separated string and write to file.
            output_content = " ".join(map(str, data_list)) if data_list else ""
            f_out.write(output_content)
    except IOError as e:
        raise RuntimeError(f"Error writing to output file '{output_file_path}': {e}") from e

if __name__ == '__main__':
    # Hard-coded sample values simulating a file with space-separated integers.
    input_data = "5 2 8 1 9 3"
    
    # Define temporary paths for this standalone execution to avoid creating files in the current directory if not desired, 
    # but per task requirements we write back to a new file path derived from the logic or hardcoded here.
    # To ensure no pre-existing files are needed and it runs without user input:
    temp_input_path = "input_numbers.txt"
    
    # Create the temporary input file with sample data before processing since the script is standalone 
    # and must run without external dependencies like pre-existing files in a clean environment.
    try:
        with open(temp_input_path, 'w') as f_temp:
            f_temp.write(input_data)
        
        sorted_numbers = read_and_sort_integers(temp_input_path)
        
        output_file_path = "sorted_output.txt"
        write_sorted_integers(sorted_numbers, output_file_path)
    finally:
        # Clean up temporary input file to ensure no side effects on the filesystem outside this run.
        if os.path.exists(temp_input_path):
            try:
                os.remove(temp_input_path)
            except OSError as e:
                print(f"Warning: Failed to remove temp input file {temp_input_path}: {e}")