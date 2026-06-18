import os

def read_numbers_from_file(filename: str) -> list[int]:
    """Read a list of integers from the specified file."""
    numbers = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Strip whitespace and skip empty lines
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                try:
                    number = int(stripped_line)
                    numbers.append(number)
                except ValueError:
                    raise ValueError(f"Invalid integer found in file at line containing: {stripped_line}")
    except FileNotFoundError:
        raise FileNotFoundError(f"The specified file '{filename}' was not found.")
    except PermissionError:
        raise PermissionError(f"No permission to read the file '{filename}'.")
    except IOError as e:
        # Catch other I/O errors (e.g., disk full, interrupted)
        raise IOError(f"An error occurred while reading from file '{filename}': {e}")

    return numbers

def is_at_least_one_positive(numbers: list[int]) -> bool:
    """Check if at least one number in the list is positive."""
    for num in numbers:
        if num > 0:
            return True
    return False

if __name__ == '__main__':
    # Hard-coded sample values to satisfy requirements without user input or files.
    # Simulating reading from a file by using an in-memory list directly, 
    # but structured as if the function returned data read from a hypothetical file.
    
    # In a real scenario with actual files:
    # numbers = read_numbers_from_file('numbers.txt')
    
    # For this standalone execution without pre-existing files or user input:
    sample_data_str = """10
-5
3
2"""

    try:
        lines = [line.strip() for line in sample_data_str.splitlines()]
        numbers = []
        for line in lines:
            if not line:
                continue
            num = int(line)
            numbers.append(num)
        
        result = is_at_least_one_positive(numbers)

        print(f"Numbers read: {numbers}")
        print(f"At least one number is positive: {result}")
    except ValueError as e:
        # This handles cases where the sample data might not be valid integers, 
        # though our hardcoded string above ensures validity.
        raise RuntimeError("Error processing sample numbers: " + str(e)) from None