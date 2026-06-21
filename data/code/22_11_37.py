def is_odd(n):
    return n % 2 != 0

if __name__ == '__main__':
    test_values = [-10, -9, 0, 1, 2, 3, 4, 5, 6]
    for value in test_values:
        result = is_odd(value)
        print(f"The number {value} is odd: {result}")