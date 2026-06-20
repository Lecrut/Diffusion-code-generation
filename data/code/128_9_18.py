def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [-15, 10, -20, 30, 0]
    for val in test_values:
        result = is_negative(val)
        print(f"Value {val} is negative: {result}")