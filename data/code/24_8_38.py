def is_negative(num):
    return num < 0

if __name__ == '__main__':
    test_values = [10, -5, 0, -3.5, 7]
    for value in test_values:
        print(is_negative(value))