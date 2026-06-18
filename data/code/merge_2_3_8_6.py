def is_even(n):
    return n & 1 == 0
if __name__ == '__main__':
    test_values = [0, 1, -2, 3, 4]
    for val in test_values:
        print(f"{val}: {is_even(val)}")