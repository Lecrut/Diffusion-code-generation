def is_odd(n):
    remainder = n % 2
    return remainder != 0

if __name__ == '__main__':
    test_cases = [10, -5, 7, 8, -10]
    for number in test_cases:
        result = is_odd(number)
        print(f"{number} is odd: {result}")