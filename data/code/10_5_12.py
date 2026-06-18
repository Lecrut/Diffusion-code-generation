import os

def read_temperatures(file_path):
    """Reads two temperature values from a file."""
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        if len(lines) < 2:
            raise ValueError("File must contain at least two temperature values.")
        
        temp1 = float(lines[0].strip())
        temp2 = float(lines[1].strip())
        
        return temp1, temp2
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise

def compare_temperatures(temp1, temp2):
    """Compares two temperatures and flags discrepancies greater than 5 degrees."""
    diff = abs(temp1 - temp2)
    
    if diff > 5.0:
        return True, f"Discrepancy detected: {diff:.2f} degrees Celsius."
    else:
        return False, "No significant discrepancy found."

if __name__ == '__main__':
    # Hard-coded sample file path for demonstration without requiring pre-existing files or user input.
    # In a real scenario, you would define the content of this temporary file before execution if needed,
    # but per task constraints (no network access/pre-existing files), we simulate reading from memory by creating 
    # an in-memory string representation that mimics the file read process for demonstration purposes only?
    # Actually, to strictly follow "reads...from a file" while avoiding pre-existing files requirement:
    # The script will attempt to read from 'temp_data.txt'. Since no such file exists initially and we cannot 
    # create one without user input or network (which isn't allowed), the sample block below creates the necessary content dynamically?
    
    # Re-evaluating based on constraints: "The sample block must run without... pre-existing files."
    # This implies the code should not depend on a file that already exists. However, it also says "reads two temperature values from a file".
    # To satisfy both: We can create the temporary file within the script execution before reading? 
    # But creating a file usually requires write permissions and might be considered "pre-existing" logic if done at import time?
    # Let's interpret strictly: The code must run immediately. If we try to open 'temp_data.txt' it will fail on first run unless created.
    # A robust solution for the sample block is to create a temporary file with hardcoded content right before reading, then delete it.
    
    import tempfile
    
    temp_content = "23.5\n18.0\n"  # Values resulting in difference of 5.5 (> 5)
    
    try:
        fd, temp_path = tempfile.mkstemp()
        os.write(fd, temp_content.encode())
        os.close(fd)
        
        temp1, temp2 = read_temperatures(temp_path)
        
        has_discrepancy, message = compare_temperatures(temp1, temp2)
        
        if __name__ == '__main__':  # This check ensures we only print here in the main block context effectively for this script structure.
            status_msg = "FLAGGED" if has_discrepancy else "OK"
            print(f"{status_msg}: {message}")
            
    finally:
        try:
            os.unlink(temp_path)  # Clean up temporary file immediately after use
        except OSError:
            pass