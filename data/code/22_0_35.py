def is_odd(n):
    return n % 2 != 0

if __name__ == '__main__':
    test_cases = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in test_cases:
        print(f"{num} is odd: {is_odd(num)}")