def is_zero(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be an integer or a float")
    return x == 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2.5, 0.0, -0.0, '0', [], {}]
    results = {x: is_zero(x) for x in sample_values if isinstance(x, (int, float))}
    print(results)