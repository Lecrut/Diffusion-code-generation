def is_value_zero(value):
    return value == 0

if __name__ == '__main__':
    test_values = [0, 1, -2, 3.14, 0j]
    for val in test_values:
        result = is_value_zero(val)
        print(f"Value {val} is zero: {result}")