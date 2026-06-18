import cmath
def validate_positivity(value):
    try:
        real_part = value.real
        return real_part > 0
    except AttributeError:
        raise TypeError("Input must be a number (int, float, or complex).")
if __name__ == '__main__':
    test_cases = [5.0, -3, cmath.rect(1, 0), cmath.rect(-2, 0)]
    for case in test_cases:
        result = validate_positivity(case)
        print(f"Input: {case}, Is Positive (Real Part > 0): {result}")