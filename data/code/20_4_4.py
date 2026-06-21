def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [4, 7, -2, 0, 15, 100]
    for value in test_values:
        result = is_even(value)
        print(f"{value}: {result}")