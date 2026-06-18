def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [1, 2, -3, 4]
    results = []
    for val in test_cases:
        result = is_even(val)
        print(f"is_even({val}) = {result}")