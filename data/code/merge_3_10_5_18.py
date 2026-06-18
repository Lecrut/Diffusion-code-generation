import os
from pathlib import Path

def read_temperature_values(filename):
    """Reads two temperature values from a CSV file."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
        
        lines = [line for line in content.split('\n') if line.strip()]
        
        # Ensure at least two values are present or handle empty file gracefully
        if len(lines) < 2:
            raise ValueError(f"Expected exactly two temperature values, got {len(lines)}.")
            
        return float(lines[0].strip()), float(lines[1].strip())
    
    except FileNotFoundError as e:
        print(f"{e}")

def compare_temperatures(t1, t2):
    """Compares two temperatures and flags discrepancies greater than 5 degrees."""
    difference = abs(t1 - t2)
    
    if difference > 5.0:
        return True
    else:
        return False

if __name__ == '__main__':
    # Hard-coded sample values for demonstration since no files are allowed to exist during execution.
    temp_1 = 23.5
    temp_2 = 28.7
    
    discrepancy_found = compare_temperatures(temp_1, temp_2)

    if discrepancy_found:
        print(f"Discrepancy detected between {temp_1} and {temp_2}.")
        print("Difference exceeds the threshold of 5 degrees Celsius.")
    else:
        print(f"No significant discrepancy found. Difference is within 5 degrees ({abs(temp_1 - temp_2)}).")