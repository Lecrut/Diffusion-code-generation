import os

def read_temperature(filename):
    """Reads a single temperature value from a file."""
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            return float(content)
    except FileNotFoundError:
        raise ValueError(f"File '{filename}' not found.")

def compare_temperatures(file1_path, file2_path):
    """Reads two temperatures and checks for discrepancy."""
    temp_a = read_temperature(file1_path)
    temp_b = read_temperature(file2_path)
    
    difference = abs(temp_a - temp_b)
    
    if difference > 5:
        return True, f"Discrepancy detected: {temp_a}°C and {temp_b}°C differ by {difference:.1f} degrees."
    else:
        return False, "No significant discrepancy found (within 5°C)."

if __name__ == '__main__':
    # Hard-coded sample values stored in temporary files to ensure no user input or network access is needed.
    temp_a_file = 'temp_a.txt'
    temp_b_file = 'temp_b.txt'
    
    try:
        with open(temp_a_file, 'w') as f1:
            f1.write('23.5')  # Sample value for first temperature
        
        with open(temp_b_file, 'w') as f2:
            f2.write('28.0')  # Sample value for second temperature (creates a >5 degree difference)
        
        has_discrepancy, message = compare_temperatures(temp_a_file, temp_b_file)
        
        print(f"Comparison Result:")
        if has_discrepancy:
            print(message)
        else:
            print("Temperatures are consistent.")
            
    finally:
        # Clean up temporary files created for the sample run.
        try:
            os.remove(temp_a_file)
            os.remove(temp_b_file)
        except OSError:
            pass