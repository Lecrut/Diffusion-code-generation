import os

def read_numbers_from_file(file_path):
    """Reads a list of numbers from the specified file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            
            if not content:
                return []
            
            # Split by whitespace and convert to integers/floats
            numbers = [int(x) for x in content.split()]
    except FileNotFoundError:
        raise ValueError(f"File '{file_path}' does not exist.")
    except PermissionError:
        raise PermissionError(f"No permission to read file '{file_path}'.")
    except IOError as e:
        raise RuntimeError(f"I/O error occurred while reading the file: {e}")

def has_positive_number(numbers):
    """Checks if at least one number in the list is positive."""
    return any(num > 0 for num in numbers)

if __name__ == '__main__':
    # Hard-coded sample values simulating a temporary file content
    # Since we cannot rely on pre-existing files, we will simulate reading 
    # from an in-memory string as if it were the file content.
    
    # Simulated file path (will not exist physically)
    simulated_file_path = "numbers_list.txt"
    
    # In a real scenario with actual files: numbers = read_numbers_from_file(simulated_file_path)
    # For this self-contained execution without external dependencies, we simulate the content directly.
    
    sample_content_str = """-5
10
3.5
-2"""

    try:
        # Simulate reading by parsing the string as if it came from a file
        numbers_list = [int(x) for x in sample_content_str.split() + ['3', '4']] 
        # Note: The above list comprehension handles integers only, but to be robust against floats like 3.5:
        
        clean_numbers = []
        try:
            parts = sample_content_str.strip().split()
            for part in parts:
                if '.' in part:
                    val = float(part)
                else:
                    val = int(float(part)) # Handles both ints and floats safely as integers or keeps them comparable
                clean_numbers.append(val)
        except ValueError:
            raise RuntimeError(f"Invalid number format found in sample data.")

    except Exception as e:
        print(f"Error processing input: {e}")
        exit(1)

    # Determine if at least one is positive
    result = has_positive_number(clean_numbers)

    if result:
        print("At least one number in the list is positive.")
    else:
        print("No numbers in the list are positive.")