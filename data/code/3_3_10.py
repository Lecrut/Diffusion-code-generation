import sys

def convert_to_kelvin(temp: float, unit: str) -> int:
    """Convert temperature to Kelvin based on Celsius or Fahrenheit."""
    if unit.lower() == 'c':
        return round(temp + 273.15)
    elif unit.lower() in ['f', '°F']:
        # Convert F to C then to K
        celsius = (temp - 32) * 5 / 9
        return round(celsius + 273.15)
    else:
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid input(), sys.stdin.read(), etc., dependencies for execution context logic if needed outside main block, but here we use hardcoded data directly.
    # Sample lines mimicking standard input format (e.g., "25 C" or "68 F")
    samples = [
        ("25", "C"),
        ("-40", "F"),
        ("100", "c"),
        ("98.6", "°F"),
    ]

    for temp_str, unit in samples:
        try:
            temperature = float(temp_str)
            kelvin_temp = convert_to_kelvin(temperature, unit)
            print(f"{kelvin_temp} K")
        except ValueError as e:
            # In a real script this might handle malformed input differently
            pass