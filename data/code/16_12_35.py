def is_positive(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a numeric value")
    return number > 0

if __name__ == '__main__':
    test_cases = [0, -1, 2.5, -3.6, 100, "a", None, True, False]
    results = {value: is_positive(value) for value in test_cases}
    print(results)