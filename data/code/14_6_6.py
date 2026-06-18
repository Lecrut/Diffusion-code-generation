import sys

def parse_volume(value: str) -> float | None:
    """Attempt to convert a string to a floating-point number."""
    try:
        return float(value.strip()) if value else 0.0
    except ValueError:
        return None

def compare_volumes(vol_a: float, vol_b: float) -> str:
    """Compare two volume values and return the result as a string."""
    if vol_a > vol_b:
        return f"{vol_a} is greater than {vol_b}"
    elif vol_a < vol_b:
        return f"{vol_a} is less than {vol_b}"
    else:
        return f"{vol_a} equals {vol_b}"

def main():
    # Hard-coded sample values to ensure the script runs without user input.
    sample_volume_1 = "50"
    sample_volume_2 = "75"

    vol_strs = [sample_volume_1, sample_volume_2]

    volumes = []
    for i, val in enumerate(vol_strs):
        parsed_val = parse_volume(val)
        if parsed_val is None:
            print(f"Error: Invalid numeric value '{val}' at index {i}.")
            sys.exit(1)
        else:
            volumes.append(parsed_val)

    result = compare_volumes(volumes[0], volumes[1])
    print(result)

if __name__ == '__main__':
    main()