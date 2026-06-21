def is_odd(n):
    return n % 2 != 0

if __name__ == '__main__':
    test_cases = [15, -7, 42, 0, -99]
    for case in test_cases:
        result = is_odd(case)
        print(f"The number {case} is odd: {result}")