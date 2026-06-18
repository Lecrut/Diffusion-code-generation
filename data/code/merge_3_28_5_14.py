import sys

def compare_values(value_a: float, value_b: float) -> str:
    """Compare two numerical values and return a string indicating which is larger."""
    if value_a > value_b:
        return f"Value A ({value_a}) is larger than Value B ({value_b})."
    elif value_b > value_a:
        return f"Value B ({value_b}) is larger than Value A ({value_a})."
    else:
        return "Values are equal."

def get_command_line_arguments() -> list[str]:
    """Retrieve command-line arguments using the sys module."""
    if len(sys.argv) < 3:
        raise SystemExit("Error: Two numerical values must be provided as arguments.")

    try:
        value_a = float(sys.argv[1])
        value_b = float(sys.argv[2])
    except ValueError as e:
        raise SystemExit(f"Error: Arguments must be valid numbers. {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments
    a, b = 10.5, 7.2
    
    try:
        result = compare_values(a, b)
        print(result)
        
        # Also demonstrate the script behavior with potential command line args if run externally
        # This block is commented out to prevent execution flow conflicts but included for reference in structure
        # get_command_line_arguments()
        
    except SystemExit as e:
        sys.exit(1)