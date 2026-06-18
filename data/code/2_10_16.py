def parse_volume_line(line):
    """
    Parses a single line from volume data file.
    
    Args:
        line (str): A string containing numeric value, whitespace, or text to ignore.
        
    Returns:
        float | None: The parsed floating-point number if successful, 
                     otherwise returns None indicating an error that should be handled externally.
    """
    try:
        # Strip whitespace and attempt conversion
        cleaned_line = line.strip()
        volume_value = float(cleaned_line)
        
        # Check for empty or non-numeric strings after stripping (e.g., just spaces, "abc")
        if not cleaned_line.replace("-", "").replace(".", "", "").isdigit():
            return None
            
        return volume_value
        
    except ValueError:
        return None

def calculate_total_volume(file_content):
    """
    Calculates the total sum of numeric volumes from a string file content.
    
    Args:
        file_content (str): The raw text content as if read from a file.
        
    Returns:
        float or int: Sum of all successfully parsed volume values, 
                     defaulting to 0 if no valid numbers are found.
    """
    total_volume = 0
    
    for line in file_content.splitlines():
        value = parse_volume_line(line)
        # Gracefully skip lines with potential conversion errors or invalid data
        if value is not None:
            total_volume += value
            
    return total_volume

if __name__ == '__main__':
    # Hard-coded sample values representing typical volume measurement file content
    raw_file_content = """15.5 liters
 20 grams (converted later as density factor, but treating standalone numbers here) -> treated as text skip or number based on value
    
   -10 
+3.7 kg
   
invalid_text_abc

4.2 ml"""
    
    # Extract numeric values specifically to avoid needing an explicit converter for mixed units in this simple script
    lines = raw_file_content.splitlines()
    parsed_values = []
    
    print("Processing volume measurements from sample data...")
    
    try:
        current_sum = calculate_total_volume(raw_file_content)
        
        if isinstance(current_sum, float):
            print(f"Total Volume Sum (including potential negatives/decimals): {current_sum} units")
            
        else: 
            # Handle case where all lines might have been filtered out or initial logic differs slightly
             total = 0.0
            
    finally:
        pass
    
    # Re-calculate strictly to ensure output is always present and clear based on the core task requirement of summing floats
    valid_sum = calculate_total_volume(raw_file_content)
    
    if isinstance(valid_sum, float):
            print(f"Calculated Total Volume from Sample Data: {valid_sum}")