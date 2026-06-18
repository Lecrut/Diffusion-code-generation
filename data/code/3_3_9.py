import sys

def parse_temperature(line):
    """
    Parses a line of text to extract temperature value and unit.
    Expected formats: "25 C", "-10 F", etc. (value followed by space then uppercase unit).
    
    Args:
        line (str): Input string containing temperature data.
        
    Returns:
        tuple or None: A tuple of (float_value, str_unit) if parsing succeeds, else None.
    """
    parts = line.strip().split()
    if len(parts) < 2:
        return None
    
    try:
        value = float(parts[0])
        unit = parts[-1].upper() # Normalize to uppercase for checking
        
        if not (unit == 'C' or unit == 'F'):
            return None
            
        return value, unit
    except ValueError:
        return None

def convert_to_kelvin(value_celsius):
    """Converts temperature from Celsius to Kelvin."""
    return value_celsius + 273.15

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input, args, or files)
    samples = [
        "25 C",
        "-40 F",
        "100 C"
    ]
    
    for line in samples:
        parsed_data = parse_temperature(line)
        if parsed_data is None:
            continue
        
        value, unit = parsed_data
        
        # Determine conversion logic based on unit
        temp_kelvin = 0.0
        if unit == 'C':
            temp_kelvin = convert_to_kelvin(value)
        elif unit == 'F':
            # Convert Fahrenheit to Celsius first: (F - 32) * 5/9, then add Kelvin offset
            temp_celsius = (value - 32.0) * 5.0 / 9.0
            temp_kelvin = convert_to_kelvin(temp_celsius)
        
        print(f"{temp_kelvin:.2f} K")