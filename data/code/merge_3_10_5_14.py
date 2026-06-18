import os

def read_temperature(filename):
    """Reads a temperature value from a file."""
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            return float(content)
    except FileNotFoundError:
        raise ValueError(f"File '{filename}' not found.")

def compare_temperatures(t1, t2):
    """Compares two temperatures and flags discrepancies greater than 5 degrees."""
    difference = abs(t1 - t2)
    if difference > 5:
        return True, f"Difference of {difference:.2f}°C exceeds the threshold."
    else:
        return False, "Difference is within acceptable limits."

if __name__ == '__main__':
    # Hard-coded sample values simulating file reads since no pre-existing files are allowed.
    temp_a = 20.5
    temp_b = 16.8
    
    discrepancy_flagged, message = compare_temperatures(temp_a, temp_b)
    
    if discrepancy_flagged:
        print(f"FLAGGED: {message}")
    else:
        print("No significant temperature difference detected.")