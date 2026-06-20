def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [-5, -1, 0, 1, -0.001]
    for val in test_values:
        print(f"is_negative({val}) is {is_negative(val)}")