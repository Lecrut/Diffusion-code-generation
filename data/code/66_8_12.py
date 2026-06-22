def convert_km_to_m(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Input must be a number.")
    if kilometers < 0:
        raise ValueError("Input must be a non-negative number.")
    return kilometers * 1000

if __name__ == '__main__':
    test_values = [1, 0, 2.5, 100]
    for value in test_values:
        result = convert_km_to_m(value)
        print(result)
    try:
        convert_km_to_m(-5)
    except ValueError as e:
        print(e)
    try:
        convert_km_to_m("abc")
    except ValueError as e:
        print(e)