def contains_negative(test_cases):
    return any(case < 0 for case in test_cases)

if __name__ == '__main__':
    sample_test_cases = [10, -5, 0, -1.5]
    result = contains_negative(sample_test_cases)
    print(f"Test cases contain negative values: {result}")