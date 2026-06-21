def is_negative(x):
    return x < 0

if __name__ == '__main__':
    test_values = [-10, -1, 0, 1, 5]
    for value in test_values:
        print(is_negative(value))