def contains_negative(test_cases):
    return any(value < 0 for value in test_cases)

if __name__ == '__main__':
    sample_test_cases = [1, -2, 3, 4, -5]
    print(contains_negative(sample_test_cases))