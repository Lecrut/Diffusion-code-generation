import sys

def compare_values(val_a: float, val_b: float) -> str:
    """Compare two numerical values and return a result string."""
    if val_a > val_b:
        return "Value A is larger"
    elif val_b > val_a:
        return "Value B is larger"
    else:
        return f"Values are equal ({val_a})"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments
    sample_value_a = 10.5
    sample_value_b = 7.2
    
    result = compare_values(sample_value_a, sample_value_b)
    print(result)