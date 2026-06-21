def is_even(n):
    if n & 1:
        return False
    return True

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 5, -1, -2]
    for val in test_values:
        print(is_even(val))