import sys

def parse_temperature(value: str) -> float | None:
    """Attempt to convert a string into a floating-point number."""
    try:
        return float(value.strip())
    except ValueError:
        return None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    temp_a = "25"
    temp_b = "-10"

    val_a = parse_temperature(temp_a)
    val_b = parse_temperature(temp_b)

    if not isinstance(val_a, (int, float)) or not isinstance(val_b, (int, float)):
        print("Error: Invalid temperature values provided.")
        sys.exit(1)

    if val_a > val_b:
        result_msg = "Temperature A is higher."
    elif val_a < val_b:
        result_msg = "Temperature B is higher."
    else:
        result_msg = "Temperatures are equal."

    print(f"Comparison of {val_a}°C and {val_b}°C:\n{result_msg}")