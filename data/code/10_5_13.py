import os

def read_temperature(filename):
    """Reads a temperature value from a file."""
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            return float(content)
    except FileNotFoundError:
        raise ValueError(f"File {filename} not found.")

def compare_temperatures(temp1, temp2):
    """Compares two temperatures and flags discrepancies greater than 5 degrees."""
    discrepancy = abs(temp1 - temp2)
    if discrepancy > 5:
        return True, f"Discrepancy of {discrepancy:.2f}°C detected."
    else:
        return False, "No significant temperature discrepancy found."

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    temp_a = 20.5
    temp_b = 16.8
    
    print(f"Comparing temperatures: {temp_a}°C and {temp_b}°C")
    
    has_discrepancy, message = compare_temperatures(temp_a, temp_b)
    
    if has_discrepancy:
        print(message)
    else:
        print("Temperatures are within the acceptable range.")