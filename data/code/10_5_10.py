import os

def read_temperatures(filename):
    """Reads two temperature values from a file."""
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        
        if len(lines) < 2:
            raise ValueError("File must contain at least two temperature values.")
            
        temp1 = float(lines[0])
        temp2 = float(lines[1])
        
        return temp1, temp2
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)

def compare_temperatures(temp1, temp2):
    """Compares two temperatures and flags discrepancies greater than 5 degrees."""
    difference = abs(temp1 - temp2)
    
    if difference > 5.0:
        print(f"DISCREPANCY DETECTED")
        print(f"Difference between {temp1}°C and {temp2}°C is {difference:.2f}°C.")
        return True
    else:
        print("No significant discrepancy found (within 5°C).")
        return False

if __name__ == '__main__':
    # Hard-coded sample values for testing without external files or user input
    temp1 = 20.5
    temp2 = 23.8
    
    print(f"Comparing temperatures: {temp1}°C and {temp2}°C")
    
    discrepancy_found = compare_temperatures(temp1, temp2)