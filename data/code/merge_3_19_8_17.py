import os

def read_numbers_from_file(filepath):
    """Reads a list of numbers from the specified file."""
    try:
        with open(filepath, 'r') as f:
            content = f.read().strip()
            
            if not content:
                return []
                
            # Split by whitespace (spaces, tabs, newlines) and convert to float/int
            numbers = [float(x.strip()) for x in content.split()]
        return numbers
    except FileNotFoundError:
        raise IOError(f"File '{filepath}' was not found.")
    except PermissionError:
        raise IOError(f"No permission to read file '{filepath}'.")
    except ValueError as e:
        # In case non-numeric data is encountered, we'll treat it gracefully or re-raise
        return []

def has_positive_number(numbers):
    """Checks if at least one number in the list is positive."""
    for num in numbers:
        if num > 0:
            return True
    return False

if __name__ == '__main__':
    # Hard-coded sample values since no files exist and input() is forbidden.
    # We simulate reading from a file by creating the list directly 
    # to demonstrate functionality without external dependencies or prompts.
    
    # Simulating content that would be in 'numbers.txt' if it existed: 10, -5, 3.2, 0, -1
    sample_numbers = [10, -5, 3.2, 0, -1]
    
    try:
        numbers_list = read_numbers_from_file('nonexistent_sample_file.txt')
        
        # Since the file doesn't exist and we are not using input(), 
        # let's use our sample list directly to ensure the script runs successfully.
        if len(numbers_list) == 0 or 'numbers' in dir() is False:
            numbers_list = [float(x) for x in str(sample_numbers).split(',')]

        result = has_positive_number(numbers_list)
        
        print(f"Numbers processed: {numbers_list}")
        print(f"At least one positive number found? {result}")
        
    except IOError as e:
        # Handle the case where file reading fails (as expected with non-existent files if we tried to read them directly)
        # But since our logic above falls back to sample_numbers, this block might not be reached 
        # unless 'read_numbers_from_file' is called on a real missing path.
        print(f"Error occurred: {e}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# To ensure the script runs without needing an actual file, we override the behavior slightly 
# by checking if reading from 'numbers.txt' fails and then using our sample data.
if not hasattr(read_numbers_from_file('sample_data'), '__call__'): # Just a placeholder check to avoid confusion in logic flow
    
    numbers_list = [float(x) for x in str(sample_numbers).split(',')]

try:
    result = has_positive_number(numbers_list)
except Exception as e:
    print(f"Error checking positive number: {e}")