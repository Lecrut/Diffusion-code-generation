def inches_to_cm(inches):
    if not isinstance(inches, (int, float)):
        raise TypeError("Input must be a numeric value.")
    return inches * 2.54

if __name__ == '__main__':
    sample_inches = 10
    try:
        cm = inches_to_cm(sample_inches)
        print(f"{sample_inches} inches is equal to {cm:.2f} centimeters")
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)