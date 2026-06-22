def is_even(n):
    result = (n & 1) == 0
    return result

if __name__ == '__main__':
    test_cases = [10, -15, 24, 37, 0, -8]
    for number in test_cases:
        print(f"{number} is even: {is_even(number)}")