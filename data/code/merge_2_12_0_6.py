def is_odd(n):
    return n & 1 != 0
if __name__ == '__main__':
    test_cases = [-5, -2, 0, 3, 7]
    for val in test_cases:
        print(f"{val}: {is_odd(val)}")