def read_volume_from_file(filename):
    """Reads volume measurements from a file and returns total volume."""
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        total_volume = 0.0
        
        for line in lines:
            # Strip whitespace including newlines
            value_str = line.strip()
            
            if not value_str or value_str.startswith('#'):
                continue
            
            try:
                volume_value = float(value_str)
                total_volume += abs(volume_value)  # Assuming absolute values as "volume" is typically positive
                
            except ValueError:
                print(f"Warning: Skipping invalid line '{value_str}' - could not convert to float.")
            
        return total_volume
        
    except FileNotFoundError:
        raise RuntimeError(f"File '{filename}' was not found.")
    except IOError as e:
        raise RuntimeError(f"Error reading file '{filename}': {e}")

def main():
    # Hard-coded sample values simulating a volume measurement log
    # This block runs without user input, command-line arguments, network access, or pre-existing files.
    
    sample_data = [
        "100",
        "# This is a comment line to be ignored",
        "-50.5",  # Negative value (handled gracefully)
        "",      # Empty line
        "invalid text here",  # Invalid float conversion test
        "250.75"
    ]

    # Create an in-memory file-like object for testing purposes since no pre-existing files are allowed
    import io
    
    input_stream = io.StringIO('\n'.join(sample_data))
    
    # Since we cannot use sys.stdin or interactive prompts, and the task requires reading from a "file",
    # we will simulate the file read by writing to a temporary string buffer.
    # However, strictly adhering to "no pre-existing files" means we shouldn't rely on disk I/O 
    # for this specific execution context unless specified otherwise in environment setup.
    # To make it truly runnable as requested with no external dependencies or files:
    
    # We will simulate the file content directly within a temporary string that mimics reading from a file object,
    # but since we can't create temp files on disk without potential cleanup issues and "no pre-existing files" constraint 
    # implies avoiding reliance on them for logic flow in this isolated run:
    
    # Let's construct the 'file' content as if it were read.
    # To strictly follow "reads volume measurements from a file", we will write to a temporary string buffer 
    # and pass that, but since standard open() requires a real path or existing object...
    # We will use an in-memory approach by simulating the file reading logic directly for the sample block.
    
    content = '\n'.join(sample_data) + "\n"

    # Simulate file read using StringIO to avoid disk I/O requirements while satisfying "reads from a file" conceptually
    import io as io_module
    
    temp_file_obj = io_module.StringIO(content)
    
    # Override the open function temporarily or just use the string content directly in our logic 
    # by treating it as if we opened 'sample_data.txt' which doesn't exist on disk.
    # To keep it simple and robust without external files:
    
    try:
        with io_module.StringIO(content) as f:
            lines = f.readlines()
            
            total_volume = 0.0
            
            for line in lines:
                value_str = line.strip()
                
                if not value_str or value_str.startswith('#'):
                    continue
                
                try:
                    volume_value = float(value_str)
                    total_volume += abs(volume_value)
                    
                except ValueError:
                    print(f"Warning: Skipping invalid measurement '{value_str}' - could not convert to float.")
            
            # Output the result for verification within this script execution
            print("Total Volume Calculated:", total_volume)

    except Exception as e:
        if "StringIO" in str(type(e)) or isinstance(e, ValueError):
             pass 
        else:
            raise

if __name__ == '__main__':
    main()