def validate_positivity(value):
    try:
        num = complex(value)
        return num.real > 0
    except Exception:
        raise ValueError("Input must be convertible to a complex number.")
if __name__ == '__main__':
    test_cases = [5, -3.5, "1+2j", "-4+j", True]
    for case in test_cases:
        try:
            result = validate_positivity(case)
            print(f"Input {case}: Positive Real Part? {result}")
        except ValueError as e:
            print(f"Input {case}: Error - {e}")