def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [0, -1, -2, 3, 4, 15, 16]
    for value in test_values:
        print(f"{value} is even: {is_even(value)}")