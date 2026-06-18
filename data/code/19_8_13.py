import os

def read_numbers_from_file(file_path):
    """Reads a list of numbers from the specified file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            
            # Handle empty files or files with no valid numbers
            if not content:
                return []
            
            # Split by whitespace and convert to integers/floats
            numbers = [int(x) for x in content.split()]
        return numbers
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied to read the file '{file_path}'.")
    except ValueError as ve:
        # In case of non-numeric strings in the list, though task implies numbers are expected.
        # We will treat it gracefully by catching and re-raising with context if needed, 
        # but for a robust script we might want to skip or raise clearly.
        # Given "handle file I/O errors", let's focus on IO, but ValueError covers content parsing too.
        raise type(ve)(f"Error converting input data: {str(ve)}") from ve

def has_positive_number(numbers):
    """Checks if at least one number in the list is positive."""
    for num in numbers:
        if num > 0:
            return True
    return False

if __name__ == '__main__':
    # Hard-coded sample values as per requirement (no user input, args, or pre-existing files needed)
    file_path = "numbers_data.txt"
    
    try:
        numbers_list = read_numbers_from_file(file_path)
        
        if not numbers_list:
            print(f"No valid numbers found in {file_path}.")
        else:
            is_positive_found = has_positive_number(numbers_list)
            
            if is_positive_found:
                print("At least one number in the list is positive.")
            else:
                print("No positive numbers were found in the list.")
    except FileNotFoundError as fnfe:
        # This handles missing files gracefully without crashing immediately, 
        # but since we can't create a file at runtime per "no pre-existing files" rule for execution context,
        # and input() is forbidden. The script must handle the state where the file doesn't exist.
        print(f"Error: {fnfe}")
    except PermissionError as pe:
        print(f"I/O Error (Permission): {pe}")
    except ValueError as ve:
        print(f"I/O/Data Error during parsing: {ve}")