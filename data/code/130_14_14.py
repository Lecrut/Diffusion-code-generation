def is_zero(num):
    return num == 0

if __name__ == '__main__':
    test_values = [0, 5, -1.5, 1e-09]
    for value in test_values:
        print(is_zero(value))