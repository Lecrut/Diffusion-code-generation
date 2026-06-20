def is_negative(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Invalid input: Expected an integer or float")
    return number < 0

if __name__ == '__main__':
    test_cases = [-5.0, 0, 3.14]
    for case in test_cases:
        try:
            print(is_negative(case))
        except ValueError as e:
            print(e)