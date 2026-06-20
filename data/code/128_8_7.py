def check_negativity(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")
    return value < 0

if __name__ == '__main__':
    test_values = [10, -5, 20, -1, 33, -12, 0]
    for val in test_values:
        print(f"Value: {val}, Is Negative: {check_negativity(val)}")