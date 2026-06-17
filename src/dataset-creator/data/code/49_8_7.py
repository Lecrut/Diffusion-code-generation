def validate_positivity(value):
    try:
        num = complex(value)
        return num.real > 0
    except (ValueError, TypeError):
        raise ValueError("Input must be convertible to a complex number.")
if __name__ == '__main__':
    test_cases = [5.5, -3.2, "1+2j", "-4+j", True]
    for case in test_cases:
        try:
            result = validate_positivity(case)
            print(f"{case}: {'Positive' if result else 'Not Positive'}")
        except ValueError as e:
            print(f"Error with {case}: {e}")