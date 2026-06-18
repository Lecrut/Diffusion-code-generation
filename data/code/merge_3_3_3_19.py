import sys

def parse_and_convert(line):
    """
    Parses a line containing temperature data in format 'value unit' 
    (e.g., "25 C") and converts it to Kelvin, returning the result as float.
    
    Supported units: C (Celsius), F (Fahrenheit)
    Raises ValueError if parsing fails or unsupported unit is found.
    """
    parts = line.strip().split()
    if len(parts) != 2:
        raise ValueError(f"Invalid format: {line}")
    
    try:
        value = float(parts[0])
    except ValueError:
        raise ValueError(f"Cannot convert '{parts[0]}' to a number")

    unit = parts[1].upper()
    
    if unit == 'C':
        return value + 273.15
    elif unit == 'F':
        # Convert Fahrenheit to Celsius then to Kelvin: (F - 32) * 5/9 + 273.15
        celsius = (value - 32) * 5 / 9
        return celsius + 273.15
    else:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units are C and F.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files
    samples = [
        "0 C",      # 273.15 K
        "100 C",    # 373.15 K
        "-40 F",    # 233.16 K (Note: -40°F equals -40°C) -> (-40-32)*5/9 + 273.15 = 233.15... wait, let's recalculate carefully
        # Recalculation for -40 F: (-40 - 32) * 5 / 9 = -72 * 5 / 9 = -8. Wait, math error in thought process above? 
        # Let's re-verify logic mentally just to be safe before outputting code.
        # Formula check: K = (F + 459.67) * 5/9 approx or F->C then C+273.15
        # -40 F -> (-40 - 32) / 1.8 = -72 / 1.8 = -40 Celsius. Correct. 
        # So K should be -40 + 273.15 = 233.15.
        
        "212 F",    # 373.15 K (Boiling point of water)
        "-40 C"     # 233.15 K
    ]

    for sample in samples:
        try:
            kelvin_temp = parse_and_convert(sample)
            print(f"{kelvin_temp:.2f} K")
        except ValueError as e:
            print(f"Error processing '{sample}': {e}", file=sys.stderr)