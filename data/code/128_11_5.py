def is_negative(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Invalid input: Expected an integer or float")
    return value < 0

if __name__ == '__main__':
    test_cases = [-5.0, 0, 3.14]
    for case in test_cases:
        try:
            result = is_negative(case)
            print(f"is_negative({case}) = {result}")
        except ValueError as e:
            print(e)