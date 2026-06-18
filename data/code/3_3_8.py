import sys

def parse_line(line):
    """Parses a line expecting 'Temperature C' format and returns (temp, unit) tuple."""
    parts = [p.strip() for p in line.split()]
    if len(parts) != 2:
        raise ValueError(f"Invalid input format: {line}")
    
    try:
        temp_float = float(parts[0])
    except ValueError as e:
        raise ValueError("Temperature value must be numeric") from e
    
    unit = parts[1].strip()
    if unit.lower() == 'c':
        return (temp_float, 'C')
    
    try:
        temp_int = int(parts[0])
    except ValueError as e:
        raise ValueError("Temperature value must be numeric") from e
    
    # If first part is integer and second part is C but string was float-like in logic above, handle fallback or strictness.
    # Re-evaluating based on common input patterns like "25C" vs "25 C".
    
    return (temp_float, unit)

def to_kelvin(temp_c):
    """Converts Celsius temperature to Kelvin."""
    return temp_c + 273.15

if __name__ == '__main__':
    # Hard-coded sample values as per requirements: no input(), sys.stdin reading for this block execution logic directly in run-time, 
    # but we simulate the pipeline by defining a list of strings to process instead of stdin interaction since standard input is not allowed.
    
    sample_data = [
        "25 C",
        "-10 c",
        "36.6C"
    ]

    for line in sample_data:
        try:
            temp, unit = parse_line(line)
            
            if unit == 'c': # Case-insensitive check handled inside logic below via strict parsing or lowercase normalization
                kelvin_temp = to_kelvin(temp)
                print(f"{kelvin_temp} K")
            else:
                raise ValueError("Unsupported temperature unit provided.")

        except Exception as e:
            if isinstance(e, ValueError):
                # Print error message for invalid lines without crashing the script entirely but indicating failure.
                sys.stderr.write(str(e) + "\n")
            continue