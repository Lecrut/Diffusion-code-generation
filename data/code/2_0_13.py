import os

def read_volume_file(file_path):
    """
    Reads volume measurements from a file line by line, parses floats,
    and returns the total sum along with any encountered errors or skipped lines.
    
    Args:
        file_path (str): Path to the file containing numeric values.
        
    Returns:
        tuple: (total_volume, error_messages) where error_messages is a list of strings.
               If an exception occurs during reading, total_volume will be 0 and errors populated.
    """
    if not os.path.exists(file_path):
        return None, [f"File '{file_path}' does not exist."]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            total_volume = 0.0
            error_messages = []
            
            for line_num, line in enumerate(f, start=1):
                stripped_line = line.strip()
                
                # Skip empty lines or comments (lines starting with #)
                if not stripped_line or stripped_line.startswith('#'):
                    continue
                
                try:
                    value = float(stripped_line)
                    total_volume += value
                except ValueError as e:
                    error_messages.append(f"Line {line_num}: Invalid number '{stripped_line}' - {e}")

            return total_volume, error_messages
            
    except PermissionError:
        return None, [f"Permission denied to read file '{file_path}'."]
    except IOError as e:
        return None, [f"I/O error while reading file '{file_path}': {e}"]

def calculate_total_volume(volume_data):
    """
    Calculates the total volume from a list of individual measurements.
    
    Args:
        volume_data (list[float]): List of float values representing volumes.
        
    Returns:
        float: Sum of all volumes, rounded to 4 decimal places for cleanliness.
               If empty input is provided, returns 0.0.
    """
    if not isinstance(volume_data, list):
        raise TypeError("Input must be a list.")
    
    total = sum(volume_data)
    return round(total, 4)

if __name__ == '__main__':
    # Hard-coded sample values for testing without external files or user input.
    # Simulating reading from a file by creating an in-memory dataset that mimics the output structure of read_volume_file logic but simplified 
    # to demonstrate calculation and error handling on valid data directly, as per robustness requirements.
    
    # Sample volume measurements (simulated content)
    sample_measurements = [10.5, 20.3, -5.7, "invalid", 40.9]

    try:
        total_volume = calculate_total_volume(sample_measurements)
        
        if not isinstance(total_volume, float):
            print("Error in calculation.")
        else:
            print(f"Total Volume Calculated: {total_volume}")
            
    except Exception as e:
        error_msg = f"A runtime exception occurred during volume processing: {e}"
        print(error_msg)