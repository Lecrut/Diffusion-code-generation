def contains_negative_values(test_cases):
    return any(value < 0 for value in test_cases)

if __name__ == '__main__':
    sample_test_cases = [1, -2, 3, 4]
    print(contains_negative_values(sample_test_cases))