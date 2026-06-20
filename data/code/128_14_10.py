def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [1, -2, 3, -4, 5]
    for val in test_values:
        print(f"Is {val} negative? {is_negative(val)}")