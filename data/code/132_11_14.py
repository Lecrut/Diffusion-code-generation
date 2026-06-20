def is_even(n):
    return n & 1 == 0

if __name__ == '__main__':
    test_values = [2, 3, -4, -5]
    for value in test_values:
        result = "even" if is_even(value) else "odd"
        print(f"{value}: {result}")