import sys

def parse_temperature(line):
    """Parses a line containing temperature value and unit (C, F)."""
    parts = line.strip().split()
    if len(parts) < 2:
        return None
    
    try:
        temp_value = float(parts[0])
        unit = parts[-1].upper()
        
        # Validate unit presence in the last part of the split string (e.g., "C" or "F")
        valid_units = {'C', 'F'}
        if not any(unit.endswith(u) for u in valid_units):
            return None
            
    except ValueError:
        return None
    
    return temp_value, unit

def convert_to_kelvin(temp_val, unit):
    """Converts temperature to Kelvin."""
    if unit == 'C':
        return temp_val + 273.15
    elif unit == 'F':
        # (temp - 32) * 5/9 + 273.15
        return (temp_val - 32) * 5 / 9 + 273.15
    else:
        raise ValueError(f"Unsupported temperature unit: {unit}")

def main():
    # Hard-coded sample values to ensure the script runs without user input or files
    samples = [
        "20 C",
        "-40 F",
        "98.6 F",
        "15 C"
    ]
    
    for line in samples:
        parsed_data = parse_temperature(line)
        
        if parsed_data is not None:
            temp_val, unit = parsed_data
            kelvin_temp = convert_to_kelvin(temp_val, unit)
            
            # Print the converted temperature to standard output
            print(f"{kelvin_temp:.2f} K")

if __name__ == '__main__':
    main()