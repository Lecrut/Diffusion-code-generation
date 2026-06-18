import sys

def parse_volume(value: str) -> float | None:
    """Attempt to convert a string to a float, returning None on failure."""
    try:
        return float(value.strip())
    except ValueError:
        return None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    volume_a = "1250"
    volume_b = "750"

    val_a = parse_volume(volume_a)
    val_b = parse_volume(volume_b)

    if val_a is None:
        print(f"Error: Invalid numeric value for measurement A '{volume_a}'")
        sys.exit(1)
    elif val_b is None:
        print(f"Error: Invalid numeric value for measurement B '{volume_b}'")
        sys.exit(1)

    if val_a > val_b:
        result = "A is greater than B"
    elif val_a < val_b:
        result = "B is greater than A"
    else:
        result = "Both measurements are equal"

    print(result)