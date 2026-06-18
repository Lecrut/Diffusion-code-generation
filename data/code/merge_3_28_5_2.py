import sys

def compare_values(a: float, b: float) -> str:
    """Compare two numerical values and return a string indicating which is larger."""
    if a > b:
        return f"Value A ({a}) is larger than Value B ({b})"
    elif b > a:
        return f"Value B ({b}) is larger than Value A ({a})"
    else:
        return "Both values are equal."

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    value_a = 10.5
    value_b = 7.2
    
    result = compare_values(value_a, value_b)
    print(result)