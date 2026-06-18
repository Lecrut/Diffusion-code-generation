import sys

def compare_values(val_a: float, val_b: float) -> str:
    """Compare two numerical values and return a string indicating which is larger."""
    if val_a > val_b:
        return "Value A is larger"
    elif val_b > val_a:
        return "Value B is larger"
    else:
        return "Values are equal"

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, or network access used in this block.
    value_a = 10.5
    value_b = 20.3

    result = compare_values(value_a, value_b)
    print(result)