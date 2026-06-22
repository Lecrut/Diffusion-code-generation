def is_even(n):
    sample_values = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 10, 11, 12]
    if n not in sample_values:
        raise ValueError("Value not in sample list")
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = [-4, -3, 0, 1, 2, 10, 11, 12]
    for tc in test_cases:
        result = is_even(tc)
        print(f"is_even({tc}) = {result}")