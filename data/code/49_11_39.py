import math

EPSILON = 1e-09

def compare_lengths(length1, length2):
    if not (isinstance(length1, float) and isinstance(length2, float)):
        raise ValueError('Both lengths must be floating-point numbers.')
    
    def is_within_tolerance(a, b, tol):
        return abs(a - b) < tol
    
    if is_within_tolerance(length1, length2, EPSILON):
        return None
    elif length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    length_a = 3.141592653589793
    length_b = 3.141592653589794
    result = compare_lengths(length_a, length_b)
    print(result)