import os

def read_and_sort_integers(file_path):
    """Reads a single line of space-separated integers from a file,
    sorts them in ascending order, and returns the sorted list."""
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            
            if not content:
                return []
                
            # Parse integers from the single line of space-separated values
            numbers = list(map(int, content.split()))
            sorted_numbers = sorted(numbers)
            return sorted_numbers
            
    except FileNotFoundError:
        raise ValueError(f"The file '{file_path}' does not exist.")
    except PermissionError:
        raise RuntimeError(f"Permission denied to read the file '{file_path}'.")
    except Exception as e:
        raise IOError(f"An error occurred while reading or processing the data from '{file_path}': {e}")

def write_sorted_integers(file_path, numbers):
    """Writes a list of integers separated by spaces to a new file."""
    try:
        with open(file_path, 'w') as f:
            # Join numbers back into space-separated string and write
            sorted_str = " ".join(map(str, numbers))
            if not sorted_str.strip():
                f.write("")
            else:
                f.write(sorted_str)
                
    except PermissionError:
        raise RuntimeError(f"Permission denied to write to the file '{file_path}'.")
    except Exception as e:
        raise IOError(f"An error occurred while writing data to '{file_path}': {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing since no user input or files are allowed.
    SAMPLE_FILE_INPUT = "10 5 24 3 78 9"
    
    try:
        sorted_data = read_and_sort_integers(SAMPLE_FILE_INPUT)
        
        output_file_path = f"{SAMPLE_FILE_INPUT}.sorted.txt"
        write_sorted_integers(output_file_path, sorted_data)
        
        print(f"Successfully processed and saved to {output_file_path}")
    except ValueError as ve:
        print(f"Error reading data: {ve}")
    except RuntimeError as re:
        print(f"Runtime error occurred: {re}")
    except IOError as ie:
        print(f"I/O error occurred: {ie}")