def is_even(n):
    return (n & 1) == 0
if __name__ == '__main__':
    test_cases = [42, -5, 0, 7]
    for val in test_cases:
        print(f"{val} is {'even' if is_even(val) else 'odd'}")