def check_positive(x):
    return x > 0

if __name__ == '__main__':
    test_cases = [5, -3, 0]
    results = [check_positive(val) for val in test_cases]
    assert all(results), "Test failed"