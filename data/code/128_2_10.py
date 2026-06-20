def is_negative(num):
    return num < 0

if __name__ == '__main__':
    test_values = [15, -7, 0, -200, 3.14]
    for value in test_values:
        result = is_negative(value)
        print(f"Value: {value}, Is Negative: {result}")