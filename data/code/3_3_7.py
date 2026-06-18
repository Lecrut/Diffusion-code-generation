import sys

def parse_line(line):
    """Parses a line containing temperature value and unit."""
    parts = line.strip().split()
    if len(parts) < 2:
        return None, "Invalid format"
    
    try:
        temp_value = float(parts[0])
    except ValueError:
        return None, f"Invalid number: {parts[0]}"
    
    unit_lower = parts[-1].lower()
    if unit_lower == 'c':
        # Celsius to Kelvin: K = C + 273.15
        kelvin_temp = temp_value + 273.15
        return kelvin_temp, None
    elif unit_lower in ['f', '°f']:
        # Fahrenheit to Kelvin: K = (F - 32) * 5/9 + 273.15
        celius_temp = (temp_value - 32) * 5 / 9
        kelvin_temp = celsius_temp + 273.15
        return kelvin_temp, None
    else:
        return temp_value, f"Unsupported unit: {unit_lower}"

def main():
    # Hard-coded sample values as per requirements to avoid interactive input
    samples = [
        "20 c",
        "68 F",
        "-4 C",
        "32.1 °F"
    ]
    
    for sample in samples:
        value, error = parse_line(sample)
        if not error and isinstance(value, (int, float)):
            print(f"{value:.2f} K")

if __name__ == '__main__':
    main()