import sys

def compare_values():
    """Compares two numerical values provided as command-line arguments."""
    if len(sys.argv) != 3:
        print("Usage: python script.py <value_a> <value_b>")
        return
    
    try:
        value_a = float(sys.argv[1])
        value_b = float(sys.argv[2])
        
        if value_a > value_b:
            result = f"Value A is larger ({value_a} > {value_b})"
        elif value_b > value_a:
            result = f"Value B is larger ({value_b} > {value_a})"
        else:
            result = "Values are equal"
        
        print(result)
    except ValueError:
        print("Error: Both arguments must be valid numbers.")

if __name__ == '__main__':
    # Sample block runs without user input or command-line arguments.
    compare_values()