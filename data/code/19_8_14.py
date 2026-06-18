import os

def read_numbers_from_file(file_path):
    """Reads a list of numbers from a file."""
    try:
        with open(file_path, 'r') as f:
            # Read all lines and attempt to convert each line to float/int
            content = f.read().strip()
            if not content:
                return []
            
            for line in content.splitlines():
                clean_line = line.strip()
                try:
                    num = float(clean_line)  # Support floats as well, though task implies numbers generally
                    yield num
                except ValueError:
                    continue  # Skip non-numeric lines
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except PermissionError:
        raise PermissionError(f"Permission denied to read the file {file_path}.")
    except IOError as e:
        raise OSError(f"An I/O error occurred while reading {file_path}: {e}")

def is_positive_in_list(numbers):
    """Determines if at least one number in the list is positive."""
    for num in numbers:
        if num > 0:
            return True
    return False

if __name__ == '__main__':
    # Hard-coded sample values to simulate a file named 'numbers.txt'
    # Since no pre-existing files are allowed and network access is forbidden,
    # we will create the content in-memory or use standard input redirection simulation.
    # However, strictly following "Do not include... sys.stdin", we must ensure 
    # this script runs without external dependencies like creating actual temp files 
    # at runtime if possible to satisfy "no pre-existing files" constraint fully.
    
    # To make it runnable and self-contained as a single module without requiring
    # the user to create 'numbers.txt', we can simulate reading from a temporary buffer,
    # but standard Python file I/O expects a real path or object. 
    # The prompt says "The script must handle file I/O errors" and sample block must run 
    # without pre-existing files. This implies if the code tries to read 'numbers.txt', it should fail gracefully 
    # with an error, OR we simulate the data in a way that doesn't require creating files on disk.
    
    # Let's create a temporary file in memory using tempfile module which is standard library,
    # or simply define the list directly as per "list of numbers from a file" logic but 
    # since external files aren't pre-existing, we'll use a temp file created and deleted immediately.
    import tempfile
    
    try:
        # Create a temporary file with sample data to satisfy "reads a list... from a file" requirement
        # without relying on user interaction or network.
        fd, path = tempfile.mkstemp(suffix='.txt')
        
        # Write sample positive and negative numbers (e.g., 5, -3)
        os.write(fd, b'10\n-2\n4\n') 
        os.close(fd)

        try:
            num_list = list(read_numbers_from_file(path))
            
            if is_positive_in_list(num_list):
                print("Success: At least one number in the file is positive.")
            else:
                print("Result: All numbers are non-positive or empty.")
                
            # Cleanup temp files created by mkstemp (standard practice)
        finally:
            try:
                os.unlink(path)
            except OSError:
                pass
                
    except Exception as e:
        # This block handles the case where no file is provided and we can't create one? 
        # Actually, tempfile works in-memory enough for this logic without persistence.
        print(f"Error during execution: {e}")