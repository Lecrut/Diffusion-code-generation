def is_zero(number):
    return number == 0

if __name__ == '__main__':
    test_values = [0, -0.0, 1e-300, 1, -1]
    for value in test_values:
        print(is_zero(value))