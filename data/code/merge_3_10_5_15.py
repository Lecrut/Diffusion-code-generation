import os

def read_temperature(filename):
    """Reads a temperature value from a file."""
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            return float(content)
    except FileNotFoundError:
        raise ValueError(f"File '{filename}' not found.")

def compare_temperatures(file1_name, file2_name):
    """Compares two temperature files and flags discrepancies > 5 degrees."""
    temp_a = read_temperature(file1_name)
    temp_b = read_temperature(file2_name)
    
    difference = abs(temp_a - temp_b)
    
    if difference > 5:
        print(f"DISCREPANCY DETECTED")
        print(f"{file1_name}: {temp_a}°C vs {file2_name}: {temp_b}°C (Difference: {difference:.2f}°C)")
        return True
    
    print("No significant discrepancy found.")
    return False

if __name__ == '__main__':
    # Hard-coded sample values in temporary files to ensure the script runs without user input or pre-existing files.
    temp_a = 20.5
    temp_b = 18.3
    
    try:
        with open('temp_sample_1.txt', 'w') as f:
            f.write(str(temp_a))
        
        with open('temp_sample_2.txt', 'w') as f:
            f.write(str(temp_b))
        
        discrepancy_found = compare_temperatures('temp_sample_1.txt', 'temp_sample_2.txt')
    finally:
        # Clean up temporary files to ensure no pre-existing file dependencies remain for future runs.
        try:
            os.remove('temp_sample_1.txt')
            os.remove('temp_sample_2.txt')
        except OSError:
            pass