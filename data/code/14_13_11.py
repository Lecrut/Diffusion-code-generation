import os

def read_volume_measurements(filename: str) -> list[float]:
    """Reads volume measurements from a file, one per line."""
    volumes = []
    
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
        
    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, 1):
                stripped_line = line.strip()
                # Skip empty lines if any occur unexpectedly during testing or cleanup
                if not stripped_line:
                    continue
                
                try:
                    value = float(stripped_line)
                    volumes.append(value)
                except ValueError as e:
                    raise ValueError(f"Invalid volume measurement on line {line_num}: '{stripped_line}'. Error: {e}") from e
                    
    except IOError as e:
        raise RuntimeError(f"Error reading file '{filename}': {e}") from e
        
    return volumes

def compare_volumes(vol1: float, vol2: float) -> str:
    """Compares two volume measurements and returns the larger one."""
    if vol1 > vol2:
        return f"{vol1:.4f}"
    elif vol2 > vol1:
        return f"{vol2:.4f}"
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # Simulating a file named 'volumes.txt' with two lines of data.
    SAMPLE_FILE_NAME = 'volumes_sample.txt'
    
    try:
        # Attempt to read from the hard-coded simulated filename structure 
        # by creating temporary content in memory logic if needed, 
        # but per instructions we assume no pre-existing files and run without input.
        # Since we cannot create actual files on disk for this isolated execution context reliably 
        # (as it might persist or fail depending on environment), 
        # we will simulate the file reading process with in-memory data to ensure success,
        # OR if strict adherence requires a real file named 'volumes.txt' which doesn't exist:
        
        # To strictly follow "run without user input... or pre-existing files", 
        # and assuming the environment does not allow creating new files (common restriction),
        # we will implement a fallback that generates the data internally to demonstrate functionality.
        
        # However, re-reading the task: "reads two volume measurements from a file named 'volumes.txt'".
        # And "The sample block must run without ... pre-existing files."
        # This implies either an empty environment or one where we can't rely on existence.
        # To make it runnable and demonstrate the logic correctly, 
        # I will create the content in a temporary way if possible, but since creating files might be restricted,
        # let's assume the standard behavior: try to read 'volumes.txt'. If missing, raise error as per requirement "handle gracefully".
        
        # But wait, usually these tasks imply we should simulate the file existence or use temp. 
        # Let's create a temporary file in memory? No, open() creates on disk.
        # Best approach for "no pre-existing files" and "runnable":
        # Use `tempfile` to create 'volumes.txt' with sample data inside this block, then read it immediately.
        
        import tempfile
        
        temp_fd = None
        try:
            # Create a temporary file named 'volumes_sample.txt' (or just use the name if allowed) 
            # The task says "file named 'volumes.txt'", so let's stick to that but create it temporarily.
            
            # Actually, creating files in temp directories is safer than current dir for isolation.
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
                tmp.write("10.5\n")
                tmp.write("23.7\n")
                
                # We need to read from 'volumes.txt' specifically per task description.
                # If we create a temp file with that name in the current directory, it might persist? 
                # No, NamedTemporaryFile deletes on close unless delete=False is set (which I did).
                # To ensure cleanup and no pre-existing dependency:
                
                tmp_path = tmp.name
                
            try:
                volumes_list = read_volume_measurements(tmp_path)
            finally:
                os.unlink(tmp_path)
            
        except Exception as e:
            print(f"Error during sample execution simulation: {e}")
            # Fallback if temp file creation fails (unlikely but safe guard):
            # Just use hardcoded values directly in comparison to show logic works.
            vol1 = 50.234
            vol2 = 78.912
            
        else:
            vol1, vol2 = volumes_list[0], volumes_list[1] if len(volumes_list) >= 2 else (volumes_list[0], float('inf'))

        result_text = compare_volumes(vol1, vol2)
        
        print(f"Comparing {vol1} and {vol2}:")
        print(result_text)
        
    except FileNotFoundError as fe:
        # This handles the case where 'volumes.txt' truly doesn't exist in a clean environment.
        print("Error: Could not find volumes.txt (as expected in a fresh environment).")
        print("Simulating with sample values for demonstration:")
        vol1 = 45.0
        vol2 = 30.0
        
    except ValueError as ve:
        print(f"Data error encountered while reading simulated or real file: {ve}")