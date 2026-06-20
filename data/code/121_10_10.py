import math

def compare_floats(a, b, tolerance=1e-9):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    if not isinstance(tolerance, (int, float)) or tolerance < 0:
        raise ValueError("Tolerance must be a non-negative number")
    if math.isclose(a, b, rel_tol=tolerance):
        return max(a, b)
    else:
        return a if a > b else b

if __name__ == '__main__':
    result = compare_floats(0.1 + 0.2, 0.3, tolerance=1e-9)
    print(result)