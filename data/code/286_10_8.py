def validate_inch_value(inches):
    if not isinstance(inches, (int, float)):
        raise ValueError("Input must be a numeric value.")

def inches_to_cm(inches):
    validate_inch_value(inches)
    return inches * 2.54

if __name__ == '__main__':
    sample_inches = 10
    try:
        cm = inches_to_cm(sample_inches)
        print(f"{sample_inches} inches is equal to {cm:.2f} centimeters")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)