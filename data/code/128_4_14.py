def is_negative(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be an integer or float.")
    return number < 0

if __name__ == '__main__':
    test_cases = [10, -5, 0, -1.5, 3.14, -100]
    for case in test_cases:
        print(f"The number {case} is {'negative' if is_negative(case) else 'not negative'}.")