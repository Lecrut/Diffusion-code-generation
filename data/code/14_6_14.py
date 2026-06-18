import sys

def is_numeric(value):
    """Check if a string represents a valid number."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input
    volume_a = 150.0
    volume_b = 275
    
    try:
        value_str_1 = str(volume_a)
        if not is_numeric(value_str_1):
            print("Error: First measurement must be numeric.", file=sys.stderr)
            sys.exit(1)
        
        value_str_2 = str(volume_b)
        if not is_numeric(value_str_2):
            print("Error: Second measurement must be numeric.", file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"Error processing measurements: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        # Attempt to convert back from string representation (though we know they are floats above)
        vol_a = float(value_str_1)
        vol_b = float(value_str_2)
        
        if abs(vol_a - vol_b) < 1e-9:
            print(f"{vol_a} is equal to {vol_b}")
        elif vol_a > vol_b:
            print(f"{vol_a} is greater than {vol_b}")
        else:
            print(f"{vol_a} is less than {vol_b}")

    except ValueError:
        print("Error converting measurements.", file=sys.stderr)
        sys.exit(1)