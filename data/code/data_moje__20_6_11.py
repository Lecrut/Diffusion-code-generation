def is_even(n):
    return (n & 1) == 0

if __name__ == '__main__':
    test_values = [1, 2, 3, 10, 100, 101]
    for value in test_values:
        print(is_even(value))