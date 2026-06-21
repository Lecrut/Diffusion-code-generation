def is_even(n):
    parity_map = {1: False, 0: True}
    return parity_map[n & 1]

if __name__ == '__main__':
    test_values = [12, 15, -8, 0, 101, -1]
    for value in test_values:
        print(value, is_even(value))