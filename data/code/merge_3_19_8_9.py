import os

def read_numbers_from_file(file_path):
    """Reads a list of numbers from the specified file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            
            if not content:
                return []
                
            # Split by whitespace (spaces, tabs, newlines) and convert to float/int
            numbers_str = content.split()
            try:
                numbers = [float(n) for n in numbers_str]
            except ValueError as e:
                raise RuntimeError(f"Invalid number format found in file: {e}") from e
            
        return numbers
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)
    except PermissionError:
        print(f"Error: No permission to read file '{file_path}'.")
        exit(1)
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        exit(1)

def is_at_least_one_positive(numbers):
    """Checks if at least one number in the list is positive."""
    return any(num > 0 for num in numbers)

if __name__ == '__main__':
    # Hard-coded sample values simulating a file content
    # Since no pre-existing files are allowed, we simulate reading from an in-memory buffer 
    # or use a temporary approach if the environment allows creating temp files.
    
    # To strictly adhere to "no user input" and "run without ... pre-existing files",
    # we will create a temporary file with sample data inside this block.
    
    try:
        # Create a temporary file path (cleaned up after use)
        import tempfile
        
        temp_file_path = None
        
        if os.name == 'nt':  # Windows uses \r\n usually, but split() handles it anyway
            pass
            
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
            tmp.write("10.5 -3.2 4.8")  # Sample data containing positive numbers
            temp_file_path = tmp.name
        
        try:
            file_numbers = read_numbers_from_file(temp_file_path)
            
            if is_at_least_one_positive(file_numbers):
                result_message = "At least one number in the list is positive."
            else:
                result_message = "No numbers in the list are positive."
                
            print(result_message)
        finally:
            # Clean up temporary file to ensure no pre-existing files dependency remains after script exit
            if temp_file_path and os.path.exists(temp_file_path):
                try:
                    os.unlink(temp_file_path)
                except OSError:
                    pass
                    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")