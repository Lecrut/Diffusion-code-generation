import sys

def compare_values(a: float, b: float) -> str:
    """Compare two numerical values and return a descriptive string."""
    if a > b:
        return "Value A is larger"
    elif b > a:
        return "Value B is larger"
    else:
        return "Values are equal"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or command-line arguments.
    value_a = 10.5
    value_b = 20.3
    
    result = compare_values(value_a, value_b)
    print(result)