import sys

def compare_values():
    """Compares two numerical values passed as command-line arguments."""
    if len(sys.argv) != 3:
        print("Error: Exactly two numeric arguments required.")
        return False

    try:
        value_a = float(sys.argv[1])
        value_b = float(sys.argv[2])
    except ValueError:
        print(f"Error: Invalid numbers provided. {sys.argv[1]} or {sys.argv[2]} is not a valid number.")
        return False

    if value_a > value_b:
        result_msg = f"{value_a} is larger than {value_b}"
    else:
        result_msg = f"{value_b} is larger than {value_a}"

    print(result_msg)
    return True

if __name__ == '__main__':
    # Hard-coded sample values for demonstration when no arguments are provided.
    # Simulating command-line behavior by parsing these into variables.
    value_a = 10
    value_b = 25

    if not compare_values():
        sys.exit(1)