def is_odd(n):
    return n & 1 != 0
if __name__ == '__main__':
    test_values = [5, -3, 42, -7]
    for val in test_values:
        result = "Odd" if is_odd(val) else "Even"
        print(f"{val} is {result}")