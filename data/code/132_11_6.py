def is_even(n):
    return n & 1 == 0

if __name__ == '__main__':
    test_values = [4, 5, 0, -2, -3]
    for value in test_values:
        print(f"{value}: {'even' if is_even(value) else 'odd'}")