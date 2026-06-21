def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [-10, 5, -3.14, 0, 2.718]
    for val in test_values:
        result = is_negative(val)
        print(f"is_negative({val}) = {result}")