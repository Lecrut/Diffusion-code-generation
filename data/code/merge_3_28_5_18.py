import sys

def compare_values(a: float | None = None, b: float | None = None) -> str:
    """
    Compares two numerical values and returns a string indicating which is larger.
    
    Args:
        a (float): First value to compare.
        b (float): Second value to compare.
        
    Returns:
        str: 'Value A is larger', 'Value B is larger', or an error message if invalid inputs are provided.
    """
    if a is None or b is None:
        return "Error: Both values must be provided."
    
    try:
        float(a)
        float(b)
    except ValueError as e:
        return f"Error: Invalid numeric input - {str(e)}"

    if a > b:
        return "Value A is larger"
    elif b > a:
        return "Value B is larger"
    else:
        return "Values are equal"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid any user input or file access.
    value_a = 105
    value_b = 98

    result = compare_values(value_a, value_b)
    print(result)