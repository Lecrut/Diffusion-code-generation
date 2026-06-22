def is_zero(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be an integer or a float")
    return x == 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2.5, None, '0', [], {}]
    results = {}
    for value in sample_values:
        try:
            results[value] = is_zero(value)
        except ValueError as e:
            results[value] = str(e)
    print(results)