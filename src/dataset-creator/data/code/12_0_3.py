def is_odd(n):
    return n & 1 != 0
if __name__ == '__main__':
    test_values = [-5, -2, 0, 3, 7, 8]
    for val in test_values:
        result = "O" if is_odd(val) else "E"
        print(f"{val}: {result}")