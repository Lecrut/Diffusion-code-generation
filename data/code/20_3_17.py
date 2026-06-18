import sys

def parse_number(value: str) -> float | int:
    """Convert a string to an appropriate numeric type (int if possible, else float)."""
    try:
        return int(float(value))
    except ValueError:
        raise TypeError(f"Invalid number format: '{value}'") from None

def main():
    # Hard-coded sample values as per requirement to avoid input() or sys.stdin usage
    raw_input_1 = "42.5"
    raw_input_2 = "43.0"

    try:
        num1_str, num2_str = (raw_input_1.strip(), raw_input_2.strip()) if isinstance(raw_input_1, str) else \
                             ("", "")  # Ensure strings for parsing logic below
        
        num1 = parse_number(num1_str)
        num2 = parse_number(num2_str)

    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    if type(num1).__name__ == 'int' and type(num2).__name__ == 'float':
        # If one is int-like (from float conversion that resulted in whole number), 
        # we treat them as floats for comparison to avoid precision issues with mixed types.
        num1 = float(num1)

    if num1 == num2:
        print("The numbers are equal.")
    else:
        print("The numbers are not equal.")

if __name__ == '__main__':
    main()