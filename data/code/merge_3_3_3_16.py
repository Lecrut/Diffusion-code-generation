import sys

def parse_and_convert(line):
    """
    Parses a line containing temperature and unit (C, F) and converts to Kelvin.
    Expected format: "temperature_unit" where unit is 'C' or 'F'.
    
    Args:
        line (str): Input string with temperature value and unit.
        
    Returns:
        float: Temperature in Kelvin.
        
    Raises:
        ValueError: If the input does not match expected format or contains invalid data.
    """
    parts = line.strip().split()
    
    if len(parts) != 2:
        raise ValueError(f"Invalid input format: {line}. Expected 'value_unit'.")
    
    try:
        temp_value = float(parts[0])
    except ValueError as e:
        raise ValueError(f"Invalid temperature value in '{parts}': {e}")

    unit_char = parts[-1].upper() if len(parts) > 1 else None
    
    # Ensure the last part is a valid unit character for this task context (C or F)
    if not isinstance(unit_char, str):
        raise ValueError(f"Invalid input format: {line}. Expected 'value_unit'.")

    if unit_char == 'F':
        kelvin = (temp_value - 32) * 5/9 + 273.15
    elif unit_char in ['C', 'c']:
        kelvin = temp_value + 273.15
    else:
        raise ValueError(f"Unsupported temperature unit '{unit_char}'. Supported units are C and F.")

    return kelvin

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user input or files.
    samples = [
        "25C",      # 25 degrees Celsius -> Kelvin
        "-40F",     # -40 degrees Fahrenheit -> Kelvin (same as -40 C)
        "100c",     # 100 degrees Celsius -> Kelvin
        "32.0 F"    # 32.0 degrees Fahrenheit -> Kelvin
    ]

    for sample in samples:
        try:
            kelvin_temp = parse_and_convert(sample)
            print(f"{kelvin_temp:.4f}")
        except ValueError as e:
            print(e, file=sys.stderr)