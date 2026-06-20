import math

def validate_inputs(val1, val2):
    if not (isinstance(val1, (int, float)) and isinstance(val2, (int, float))):
        raise ValueError("Both inputs must be integers or floats")
    return True

def are_floats_close(a, b, rel_tol=1e-09, abs_tol=0.0):
    validate_inputs(a, b)
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)

if __name__ == '__main__':
    print(are_floats_close(0.1 + 0.2, 0.3))
    print(are_floats_close(float('inf'), float('inf')))
    print(are_floats_close(float('nan'), float('nan')))
    print(are_floats_close(float('inf'), float('-inf')))