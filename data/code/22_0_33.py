ODD_CHECK_MODULO = 2

def is_odd(n):
    return n % ODD_CHECK_MODULO != 0

if __name__ == '__main__':
    test_values = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for value in test_values:
        print(f"{value} is odd: {is_odd(value)}")