def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [4, -3, 0]
    for case in test_cases:
        result = is_even(case)
        print(f"Number {case} is even: {result}")