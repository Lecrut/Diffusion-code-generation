def convert_to_float(value):
    """Attempts to convert a string value to a float."""
    try:
        return float(value)
    except ValueError:
        raise TypeError(f"Cannot convert '{value}' to float")

def read_and_calculate_volumes(file_path):
    """Reads volume measurements from a file and calculates the total."""
    total_volume = 0.0
    
    with open(file_path, 'r') as f:
        for line in f:
            # Strip whitespace and skip empty lines or comments starting with '#'
            stripped_line = line.strip()
            
            if not stripped_line:
                continue
            
            if stripped_line.startswith('#'):
                continue
                
            try:
                volume_value = convert_to_float(stripped_line)
                total_volume += volume_value
            except ValueError as e:
                # Gracefully handle potential float conversion errors by skipping the line
                print(f"Skipping invalid entry '{stripped_line}': {e}")
    
    return total_volume

if __name__ == '__main__':
    # Hard-coded sample data representing a temporary file with volume measurements
    sample_data = """10.5
23.4
# This is a comment line, should be ignored
invalid entry here
7.89
"""

    import tempfile
    import os
    
    # Create a temporary file to simulate the input file since we cannot use stdin or arguments
    temp_file_path = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_file:
            tmp_file.write(sample_data)
            temp_file_path = tmp_file.name
            
        # Read volumes from the temporary file and calculate total
        result_volume = read_and_calculate_volumes(temp_file_path)
        
        print(f"Total Volume Calculated: {result_volume}")
    finally:
        if temp_file_path is not None and os.path.exists(temp_file_path):
            os.remove(temp_file_path)