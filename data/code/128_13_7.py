def is_negative(num):
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a numeric value")
    return num < 0

if __name__ == '__main__':
    test_cases = [-5, -1.5, 0, 3, 3.14]
    for x in test_cases:
        try:
            result = is_negative(x)
            print(f"is_negative({x}) -> {result}")
        except ValueError as e:
            print(e)