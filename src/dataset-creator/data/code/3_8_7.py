def is_even(n):
    return not (n & 1)
if __name__ == '__main__':
    test_values = [0, 2, -3, 5, 4]
    for val in test_values:
        result = "Even" if is_even(val) else "Odd"
        print(f"{val} -> {result}")