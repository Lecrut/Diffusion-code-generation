import os

def read_temperature(filename):
    """Reads temperature values from a file."""
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            
        # Handle multiple lines or single line input
        if '\n' in content:
            temps = [float(temp.strip()) for temp in content.split('\n')]
        else:
            temps = float(content)
        
        return temps[0], temps[1]
    except FileNotFoundError:
        raise ValueError(f"File '{filename}' not found.")
    except IndexError as e:
        raise ValueError("Invalid number of temperature values provided in file.") from e

def check_temperature_discrepancy(temp1, temp2):
    """Checks if the absolute difference between two temperatures exceeds 5 degrees."""
    discrepancy = abs(temp1 - temp2)
    
    if discrepancy > 5:
        print(f"DISCREPANCY DETECTED: {temp1}°C and {temp2}°C differ by {discrepancy:.2f}°C")
        return True
    else:
        print("No significant temperature difference detected.")
        return False

if __name__ == '__main__':
    # Hard-coded sample values simulating a file named 'temperatures.txt'
    temp_file_content = "23.5\n18.0"
    
    # Simulate reading from a file using the content directly since no real files exist in this environment
    try:
        temps_a, temps_b = read_temperature('temp_data.txt')
        
        if check_temperature_discrepancy(temps_a, temps_b):
            print("Alert: Temperature discrepancy found.")
        else:
            print("Status: Temperatures are within acceptable range.")
            
    except Exception as e:
        # Handle the case where no file exists by using the hard-coded values directly for demonstration
        if "File" in str(e) or "not found" in str(e).lower():
            temps_a = 23.5
            temps_b = 18.0
            
            print("Running with simulated data (since temp_data.txt is not available):")
            
            try:
                check_temperature_discrepancy(temps_a, temps_b)
            except Exception as e2:
                raise RuntimeError(f"Error during comparison: {e2}") from e
        else:
            raise