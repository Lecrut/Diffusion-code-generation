def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [-4, -3, 0, 1, 2, 100]
    for val in test_values:
        print(is_even(val))