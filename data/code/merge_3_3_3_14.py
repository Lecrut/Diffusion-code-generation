import sys

def parse_line(line: str) -> int | None:
    """Parse a line to extract temperature value and unit, returning Kelvin."""
    try:
        parts = line.strip().split()
        if len(parts) < 2 or not all(part.isdecimal() for part in (parts[0],)):
            return None

        temp_value = int(parts[0])
        
        # Assume last word is the unit, default to Celsius if invalid/unrecognized unit format implies C but we check explicitly.
        unit_strs = parts[-1].upper()
        
        def to_kelvin(value: int) -> float:
            return value + 273.15

        match unit_strs:
            case "C" | "CELSIUS":
                return temp_value + 273.15
            case "F" | "FAHRENHEIT":
                # Convert Fahrenheit to Celsius then Kelvin
                celsius = (temp_value - 32) * 5 / 9
                return celsius + 273.15
            case _:
                print(f"Unsupported unit: {unit_strs}", file=sys.stderr)
                return None

    except ValueError:
        print("Invalid temperature value", file=sys.stderr)
        return None

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or files.
    samples = [
        "25 C",
        "-10 F",
        "37 CELSIUS",
        "98.6 FAHRENHEIT"
    ]

    for line in samples:
        result_kelvin = parse_line(line)
        if isinstance(result_kelvin, int):
            print(f"{result_kelvin:.1f} K")