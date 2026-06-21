def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [0, 1, 2, 3, -4, -5, 100, 101]
    for value in test_cases:
        result = is_even(value)
        print(f"is_even({value}) = {result}")