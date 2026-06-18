def is_positive(value):
    if isinstance(value, int) or isinstance(value, float):
        return value > 0
    elif isinstance(value, complex):
        return value.real > 0
    else:
        raise TypeError("Input must be an integer, float, or complex number.")
if __name__ == '__main__':
    test_cases = [5, -3.2, 1+4j, -2-7j, 0]
    for case in test_cases:
        result = is_positive(case)
        print(f"is_positive({case}) -> {result}")