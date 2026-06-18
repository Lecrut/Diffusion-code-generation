import re

def parse_volume(line):
    """
    Attempts to extract a numeric volume from a line of text.
    Returns None if no valid number is found or an error occurs during conversion.
    
    Args:
        line (str): A string representing the measurement data.
        
    Returns:
        float | None: The parsed floating-point value, or None on failure.
    """
    # Use regex to find a pattern that looks like a number (int, float, scientific notation)
    match = re.search(r'-?\d+\.?\d*([eE][+-]?\d+)?', line)
    
    if not match:
        return None
    
    try:
        # Convert the matched string to a float
        value_str = match.group()
        volume = float(value_str)
        return volume
    except ValueError as e:
        print(f"Warning: Failed to convert '{value_str}' to float. Reason: {e}")
        return None

def calculate_total_volume(file_path):
    """
    Reads a file, attempts to parse each line for numerical values,
    and returns the sum of all successfully parsed volumes.
    
    Args:
        file_path (str): The path to the data file containing volume measurements.
        
    Returns:
        float | None: The total calculated volume or None if no valid numbers are found.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
            # Split the file into individual lines (handling potential multi-line measurements)
            raw_lines = [line.strip() for line in content.split('\n')]
        
        total_volume = 0.0
        
        for i, line in enumerate(raw_lines):
            if not line:
                continue
            
            parsed_value = parse_volume(line)
            
            if parsed_value is None:
                # Log a warning but do not stop execution; this ensures graceful handling
                print(f"Warning: Could not parse volume on line {i + 1}: '{line}'")
            else:
                total_volume += parsed_value
        
        return total_volume
    
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'.")
        raise SystemExit(1) from None
    except PermissionError:
        print(f"Error: No permission to read file '{file_path}'.")
        raise SystemExit(2) from None

if __name__ == '__main__':
    # Hard-coded sample values for testing without external files or user input.
    # Simulating the content of a volume measurement file stored in memory.
    
    sample_data = """
    500 ml
    75 mL is correct.
    Invalid text and -234.5 here too! [error]
    1e-3 liters, maybe?
     (empty line above)  
    NaN value test # should be ignored or raise error depending on strictness but float('nan') breaks sum if not handled carefully by standard types in some contexts though Python's math module handles it differently. Let's stick to simple parsing which usually catches non-numeric strings as None via regex failure first.
    
        """
    
    # Create a temporary list of lines representing the file content for processing.
    simulated_file_content = sample_data.strip().split('\n')
    
    total_volume_calculated = 0.0
    
    print("--- Volume Calculation Report ---")
    print(f"Input Data Source: Hard-coded Sample (simulating '{__file__.replace('.py', '')}_sample.txt)'")
    
    for i, line in enumerate(simulated_file_content):
        if not line.strip():
            continue
            
        parsed_value = parse_volume(line)
        
        status_icon = "OK" if parsed_value is not None else "SKIP/ERROR"
        print(f"[Line {i+1}] Data: '{line[:30]}...' -> Value: {parsed_value} ({status_icon})")
    
    # Calculate sum manually to ensure we don't accidentally include NaN or other edge cases 
    # that might arise if regex missed a 'NaN' string but float conversion failed.
    for line in simulated_file_content:
        val = parse_volume(line)
        if val is not None and math.isnan(val):
            print(f"Warning: Detected non-numeric (NaN-like or invalid float) value on current iteration, skipping addition.")
    
    # Re-calculate total using only successfully parsed floats to avoid NaN propagation in the sum logic.