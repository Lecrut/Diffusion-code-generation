def is_positive(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be an integer or float")
    return number > 0

if __name__ == '__main__':
    test_values = [15, -7, 0.0, 4.56, -9.87, 'a', None]
    results = {}
    for value in test_values:
        try:
            results[value] = is_positive(value)
        except ValueError as e:
            results[value] = str(e)
    print(results)