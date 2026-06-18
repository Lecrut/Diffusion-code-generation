import os

def read_numbers_from_file(file_path):
    """Reads a list of numbers from the specified file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            
            if not content:
                return []
                
            # Split by whitespace and convert to integers/floats
            numbers = [int(num) for num in content.split()]
    except FileNotFoundError:
        raise ValueError(f"The file '{file_path}' does not exist.")
    except PermissionError:
        raise ValueError(f"Permission denied to read the file '{file_path}'.")
    except IOError as e:
        raise RuntimeError(f"I/O error occurred while reading {file_path}: {e}")
    
    return numbers

def has_positive_number(numbers):
    """Determines if at least one number in the list is positive."""
    for num in numbers:
        if num > 0:
            return True
    return False

if __name__ == '__main__':
    # Hard-coded sample file path (will not exist on a fresh run, triggering error handling)
    SAMPLE_FILE_PATH = "sample_numbers.txt"
    
    try:
        numbers_list = read_numbers_from_file(SAMPLE_FILE_PATH)
        
        if has_positive_number(numbers_list):
            print("Result: At least one number is positive.")
        else:
            print("Result: No positive numbers found in the list.")
            
    except ValueError as ve:
        # Handles missing file or permission errors specifically mentioned above
        print(f"Error: {ve}")
        
    except RuntimeError as re:
        # Handles generic I/O exceptions (e.g., encoding issues, disk full)
        print(f"I/O Error occurred during processing: {re}")