import math

def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return a, b

def compare_floats(a, b, tolerance=1e-9):
    a, b = validate_numbers(a, b)
    if math.isclose(a, b, rel_tol=tolerance):
        return max(a, b)
    else:
        return a if a > b else b

if __name__ == '__main__':
    result = compare_floats(0.1 + 0.2, 0.3, tolerance=1e-9)
    print(result)