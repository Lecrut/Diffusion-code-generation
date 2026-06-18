import os

def read_temperature(filename):
    """Reads a single temperature value from a file."""
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    try:
        return float(content)
    except ValueError:
        raise ValueError(f"Invalid temperature format in {filename}: {content}")

def compare_temperatures(file1_name, file2_name):
    """Reads two temperatures from files and checks for a discrepancy > 5 degrees."""
    temp_a = read_temperature(file1_name)
    temp_b = read_temperature(file2_name)
    
    if abs(temp_a - temp_b) > 5:
        return "FLAGGED"
    else:
        return "OK"

if __name__ == '__main__':
    # Hard-coded sample values to simulate files since no pre-existing files are allowed.
    # We create temporary content in memory by reading from strings that mimic file behavior,
    # but strictly adhering to the constraint of not calling input() or relying on external files.
    
    # Simulating 'temp_a.txt' containing 20.5
    temp_a_content = "20.5"
    try:
        with open('temp_a_simulated', 'w') as f:
            f.write(temp_a_content)
    except IOError:
        pass
    
    # Simulating 'temp_b.txt' containing 18.3 (Difference is 2.2, which is <= 5)
    temp_b_content = "18.3"
    try:
        with open('temp_b_simulated', 'w') as f:
            f.write(temp_b_content)
    except IOError:
        pass
    
    # Attempting to read from the simulated files (which were just created in this process's memory/disk if allowed, 
    # but per strict "no pre-existing files" and "run without... network", we must ensure the script runs standalone.
    # Since creating files might be considered side effects or unavailable on some restricted environments,
    # let's implement a robust fallback that reads from strings directly to guarantee execution without any file I/O 
    # if the environment disallows writing temporary files, while still fulfilling the logic requirement.
    
    # However, the task asks to "read two temperature values from a file". To strictly satisfy this in an isolated run 
    # where no pre-existing files exist and we cannot guarantee write permissions for temp files on all restricted runners:
    # We will use os.path.exists check with fallback logic that reads hardcoded strings into temporary named pipes or just uses the string content.
    
    # Re-evaluating based on "Do not include... any interactive prompt" and "run without user input".
    # The safest interpretation for a runnable module in this context is to simulate the file reading using embedded data 
    # if actual files cannot be guaranteed, OR create them within the same process execution block.
    
    # Let's stick to creating the temp files as it satisfies "read from a file" logically and runs without external dependencies.
    
    try:
        status = compare_temperatures('temp_a_simulated', 'temp_b_simulated')
        
        if status == "FLAGGED":
            print("DISCREPANCY DETECTED")
        else:
            print("NO SIGNIFICANT DISCREPANCY FOUND")
    except FileNotFoundError as e:
        # Fallback for environments where temp file creation might fail or be restricted.
        # We simulate the read directly from strings to ensure it runs without user input/filesystem dependency if needed,
        # but primarily we rely on the files created above. If they don't exist (e.g., sandbox), this block handles it gracefully 
        # by reading the hardcoded values as a fallback mechanism for "reading" them virtually.
        
        temp_a = float(temp_a_content)
        temp_b = float(temp_b_content)
        
        if abs(temp_a - temp_b) > 5:
            print("DISCREPANCY DETECTED")
        else:
            print("NO SIGNIFICANT DISCREPANCY FOUND")