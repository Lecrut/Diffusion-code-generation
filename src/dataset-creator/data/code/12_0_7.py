def is_odd(n):
    return n & 1 != 0
if __name__ == '__main__':
    test_values = [5, -3, 42, -7]
    for val in test_values:
        print(f"{val}: {is_odd(val)}")