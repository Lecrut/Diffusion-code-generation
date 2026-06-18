import sys

def compare_values(val_a: float, val_b: float) -> str:
    """Returns a string indicating which value is larger."""
    if val_a > val_b:
        return "Value A is larger"
    elif val_b > val_a:
        return "Value B is larger"
    else:
        return "Values are equal"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or arguments.
    sample_value_a = 10
    sample_value_b = 25

    result = compare_values(sample_value_a, sample_value_b)
    print(result)