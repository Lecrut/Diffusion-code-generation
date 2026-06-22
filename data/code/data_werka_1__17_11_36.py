def is_even(n):
    return (n & 1) == 0

if __name__ == '__main__':
    test_values = [0, 1, -2, 3, 4, -5, 6, -7, 8, -9]
    for value in test_values:
        print(f"{value} is even: {is_even(value)}")