def is_even(n):
    return (n & 1) == 0
if __name__ == '__main__':
    test_values = [0, -5, 42, -3, 100]
    for val in test_values:
        print(f"{val} is {'even' if is_even(val) else 'odd'}")