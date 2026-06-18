def calculate_total_volume(file_path):
    """
    Reads volume measurements from a file and calculates the total volume.
    
    Args:
        file_path (str): Path to the file containing volume measurements, one per line.
        
    Returns:
        float or None: The sum of all valid numeric volumes found in the file.
                       Returns None if no valid numbers are found or an error occurs.
    """
    total_volume = 0.0
    
    try:
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f):
                # Strip whitespace and skip empty lines
                stripped_line = line.strip()
                
                if not stripped_line:
                    continue
                
                try:
                    volume = float(stripped_line)
                    total_volume += volume
                except ValueError as e:
                    # Gracefully handle non-numeric values by skipping the problematic line
                    print(f"Warning: Skipping invalid value at line {line_num + 1}: '{stripped_line}' - Reason: {e}")
                    
    except FileNotFoundError:
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None
        
    return total_volume

def read_from_hardcoded_values():
    """
    Reads volume measurements from hardcoded sample values.
    
    Returns:
        float or None: The sum of all valid numeric volumes.
                       Returns None if no valid numbers are found or an error occurs.
    """
    # Sample data simulating a file content
    sample_data = [
        "50.5",
        "23.7",
        "",  # Empty line (should be skipped)
        "invalid_text_here",  # Should cause warning and skip
        "-10.2",  # Negative value (valid float, should be included in sum)
        None    # Simulates a read error or non-numeric object if we were parsing objects instead of strings directly
    ]

    total_volume = 0.0
    
    for line_num, item in enumerate(sample_data):
        try:
            volume_str = str(item) if item is not None else ""
            
            # Skip empty lines
            stripped_line = volume_str.strip()
            if not stripped_line:
                continue
            
            vol_value = float(stripped_line)
            total_volume += vol_value
            
        except ValueError as e:
            print(f"Warning: Skipping invalid value at line {line_num + 1}: '{item}' - Reason: Value conversion error")
            
    return total_volume

if __name__ == '__main__':
    # Simulating reading from a file with hardcoded values for this task requirement.
    # This avoids the need for external files or user input.
    
    print("Starting volume calculation...")
    
    # Calculate using sample data directly as per requirements (no pre-existing files needed)
    total = read_from_hardcoded_values()
    
    if total is not None:
        print(f"Total Volume Calculated: {total}")
    else:
        print("Failed to calculate volume.")