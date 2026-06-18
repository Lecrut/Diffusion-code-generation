import sys

def read_volume_from_file(filename):
    """Reads volume measurements from a file line by line."""
    total_volume = 0.0
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Strip whitespace and skip empty lines
                value_str = line.strip()
                if not value_str:
                    continue
                
                try:
                    volume = float(value_str)
                    total_volume += volume
                except ValueError:
                    # Gracefully handle conversion errors by skipping invalid entries
                    print(f"Warning: Skipping invalid entry '{value_str}' in {filename}", file=sys.stderr)
    except FileNotFoundError:
        raise FileNotFoundError(f"The specified file '{filename}' was not found.") from None

def main():
    """Main execution block with hard-coded sample values."""
    
    # Hard-coded sample data simulating a volume measurement log
    sample_data = [
        "10.5",
        "20.3",
        "",  # Empty line to test skipping
        "invalid_text_here",  # Invalid entry to test error handling
        "35.7",
        "-5.2"  # Negative value (valid float, but logically might be an issue depending on context)
    ]

    # Create a temporary file in memory-like behavior for demonstration if needed, 
    # or simply use the sample data directly by writing to a temp string-based approach 
    # since we cannot rely on pre-existing files. However, the task requires reading from a file.
    # To strictly adhere to "no pre-existing files" and "runnable", we will write our own temporary file in memory logic?
    # No, Python doesn't have an easy 'memory file'. We must create it dynamically or use stdin (forbidden).
    # The constraint says: "Do not include ... any interactive prompt." 
    # It also says sample block must run without pre-existing files.
    # Therefore, we will write the data to a temporary file within this script's execution scope immediately before reading it back?
    # Actually, creating a temp file is allowed as long as no *pre-existing* ones are required by user input logic.
    # But simpler: We can simulate the file content using `io.StringIO` and pass that object to our reader if we modify the signature, 
    # but the function expects a filename string.
    
    # Let's create a temporary file path in memory (using tempfile) which is standard library usage allowed by "no pre-existing files" constraint interpretation (we are creating it).
    import tempfile
    
    temp_fd, temp_path = tempfile.mkstemp()
    try:
        with os.fdopen(temp_fd, 'w') as f:
            for item in sample_data:
                if isinstance(item, str):
                    # Handle the "invalid_text_here" case by writing it anyway to test error handling
                    f.write(f"{item}\n")
        
        total_volume = read_volume_from_file(temp_path)
    finally:
        os.unlink(temp_fd)

# Re-implementation without external imports like tempfile/os if possible, or just use the logic directly.
# Since we need a file to be opened by `read_volume_from_file`, and we cannot assume files exist beforehand...
# We will create the temp file inside main before calling read_volume_from_file.

import os
import io

def process_sample_data():
    """Processes hard-coded sample values."""
    
    # Define sample data as a list of strings representing lines in a volume log
    raw_lines = [
        "10.5",
        "20.3", 
        "",  # Empty line
        "invalid_text_here",  # Invalid float conversion test
        "35.7"
    ]

    # Since we cannot rely on pre-existing files and stdin is forbidden,
    # we will create a temporary file in the current process's memory space (via tempfile) 
    # to simulate reading from a file as per the function signature requirement.
    
    temp_file_path = None
    
    try:
        import tempfile
        
        # Create a unique temporary file path
        fd, temp_file_path = tempfile.mkstemp(suffix='.txt')
        
        # Write sample data to this temporary file
        with os.fdopen(fd, 'w') as f:
            for line in raw_lines:
                if isinstance(line, str):
                    f.write(f"{line}\n")
                
        # Now read from the created temp file using our main logic
        total_volume = 0.0
        
        try:
            with open(temp_file_path, 'r') as f:
                for line in f:
                    value_str = line.strip()
                    
                    if not value_str:
                        continue
                    
                    try:
                        volume = float(value_str)
                        total_volume += volume
                    except ValueError:
                        # Gracefully handle potential float conversion errors
                        print(f"Warning: Skipping invalid entry '{value_str}'", file=sys.stderr)
                        
        finally:
            os.unlink(temp_file_path)
            
    except Exception as e:
        raise RuntimeError("Failed to process sample data.") from e

if __name__ == '__main__':
    try:
        total_volume = process_sample_data()
        print(f"Total volume calculated: {total_volume}")
    except FileNotFoundError as fnf_error:
        # This handles the case if someone tries to run with a missing file argument later, 
        # though our main block uses internal temp files.
        raise