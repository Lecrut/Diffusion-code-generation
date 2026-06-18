import sys

def parse_temperature(value: str) -> float | None:
    """Attempt to convert a string to a floating-point number."""
    try:
        return float(value.strip())
    except ValueError:
        return None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    temp_a_str = "25"
    temp_b_str = "-10"

    temp_a_raw = parse_temperature(temp_a_str)
    temp_b_raw = parse_temperature(temp_b_str)

    if temp_a_raw is None:
        print(f"Error: Invalid temperature '{temp_a_str}'")
        sys.exit(1)

    if temp_b_raw is None:
        print(f"Error: Invalid temperature '{temp_b_str}'")
        sys.exit(1)

    comparison_result = ""
    signs = ["", ">", "<"]
    
    # Determine the relationship between temperatures.
    if temp_a > temp_b:
        result_symbol = ">"
    elif temp_a < temp_b:
        result_symbol = "<"
    else:
        result_symbol = "="

    comparison_result = f"{temp_a} {result_symbol} {temp_b}"

    print(f"\nComparison Result:\n{comparison_result}")