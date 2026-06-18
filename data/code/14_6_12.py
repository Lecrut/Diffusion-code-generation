import sys

def read_and_validate_line(line):
    """Read a line from stdin (or raise if empty) and validate it is numeric."""
    stripped = line.strip()
    try:
        return float(stripped)
    except ValueError:
        print(f"Error: '{stripped}' is not a valid number.", file=sys.stderr)
        sys.exit(1)

def compare_volumes(volume_a, volume_b):
    """Compare two volumes and determine the result."""
    if volume_a == volume_b:
        return "Equal"
    elif volume_a > volume_b:
        return f"{volume_a} is greater than {volume_b}"
    else:
        return f"{volume_a} is less than {volume_b}"

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external files.
    SAMPLE_VOLUMES = [10.5, 25]

    try:
        volume_a = float(SAMPLE_VOLUMES[0])
        volume_b = float(SAMPLE_VOLUMES[1])
    except IndexError:
        print("Error: Not enough sample values provided.", file=sys.stderr)
        sys.exit(1)

    result_message = compare_volumes(volume_a, volume_b)
    print(f"Comparison Result: {result_message}")