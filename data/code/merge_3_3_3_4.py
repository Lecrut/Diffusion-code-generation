import sys

def parse_and_convert(line):
    """
    Parses a line containing temperature data in format 'value unit' 
    (e.g., "25 C") or just value if no unit is specified, assuming Celsius by default.
    Converts the temperature to Kelvin and returns it as a string with 2 decimal places.
    
    Args:
        line (str): Input string containing temperature data.
        
    Returns:
        str: Temperature in Kelvin formatted to two decimal places.
    """
    parts = line.strip().split()
    if not parts or len(parts) == 0:
        return "Error: Empty input"

    try:
        temp_value = float(parts[0])
        
        # Determine unit based on the last element, defaulting to Celsius (C)
        unit_str = parts[-1].upper()
        
        if unit_str in ['F', 'FAHRENHEIT']:
            # Convert Fahrenheit to Kelvin: K = (F - 32) * 5/9 + 273.15
            kelvin_temp = (temp_value - 32) * 5 / 9 + 273.15
        elif unit_str in ['C', 'CELSIUS']:
            # Convert Celsius to Kelvin: K = C + 273.15
            kelvin_temp = temp_value + 273.15
        else:
            return f"Error: Unknown unit '{unit_str}'. Supported units are C, F."

    except ValueError:
        return "Error: Invalid temperature value."

    return f"{kelvin_temp:.2f} K"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    samples = [
        "25 C",
        "-40 F",
        "100 C",
        "32 F",
        "0"  # Defaulting to Celsius as no unit is provided
    ]

    for sample in samples:
        result = parse_and_convert(sample)
        print(result)