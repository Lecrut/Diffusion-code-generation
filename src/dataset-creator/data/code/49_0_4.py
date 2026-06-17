import math
def is_positive(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be an integer or a float.")
    return value > 0 and not math.isnan(value) and not math.isinf(value)
if __name__ == '__main__':
    test_cases = [10, -5.5, 0, 3.14, float('nan'), float('-inf')]
    for case in test_cases:
        try:
            result = is_positive(case)
            print(f"Input {case}: Positive={result}")
        except TypeError as e:
            print(f"Error with input {case}: {e}")