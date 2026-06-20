def check_negative(values):
    return any(value < 0 for value in values)

if __name__ == '__main__':
    test_values = [-1, 2, 3, -4, 5]
    print(check_negative(test_values))