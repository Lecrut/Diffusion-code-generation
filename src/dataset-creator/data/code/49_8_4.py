import cmath
def is_positive(value):
    try:
        if isinstance(value, (int, float)):
            return value > 0
        elif isinstance(value, complex):
            return value.real > 0
        else:
            raise TypeError("Input must be a number.")
    except Exception as e:
        print(f"Error validating input: {e}")
        return False
if __name__ == '__main__':
    test_cases = [5, -3.2, 0, complex(4, 7), complex(-1, 9)]
    for case in test_cases:
        result = is_positive(case)
        print(f"Input: {case} -> Is Positive: {result}")