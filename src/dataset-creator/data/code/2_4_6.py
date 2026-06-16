def is_positive(value):
    return value > 0
if __name__ == '__main__':
    test_cases = [10, -5, 0, 3.14]
    for val in test_cases:
        print(f"{val}: {is_positive(val)}")