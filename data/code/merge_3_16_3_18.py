def is_positive(x):
    return x > 0

if __name__ == '__main__':
    test_cases = [3, -5, 0]
    results = []
    for val in test_cases:
        result = is_positive(val)
        print(f"is_positive({val}) = {result}")