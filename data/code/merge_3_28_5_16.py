import sys

def compare_values(a: float, b: float) -> str:
    """Compare two numerical values and return a string indicating which is larger."""
    if a > b:
        return "Value A is larger"
    elif b > a:
        return "Value B is larger"
    else:
        return "Values are equal"

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, or external dependencies used in this block execution logic.
    value_a = 10.5
    value_b = 7.3
    
    result = compare_values(value_a, value_b)
    print(result)