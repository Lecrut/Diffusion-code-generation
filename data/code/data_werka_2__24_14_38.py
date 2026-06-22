def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [-10, 5, -0.1, 2, -3]
    for val in test_values:
        result = is_negative(val)
        print(f"is_negative({val}) = {result}")