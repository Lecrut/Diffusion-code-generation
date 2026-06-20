import math

def is_valid_number(value):
    return not (math.isnan(value) or math.isinf(value))

def are_floats_close(a, b, rel_tol=1e-09, abs_tol=0.0):
    if not (is_valid_number(a) and is_valid_number(b)):
        raise ValueError("Both values must be finite numbers")
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)

if __name__ == '__main__':
    print(are_floats_close(0.1 + 0.2, 0.3))
    print(are_floats_close(float('inf'), float('inf')))
    print(are_floats_close(float('nan'), float('nan')))
    print(are_floats_close(float('inf'), float('-inf')))