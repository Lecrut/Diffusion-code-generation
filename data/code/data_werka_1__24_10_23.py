is_negative = lambda x: x < 0

if __name__ == '__main__':
    test_cases = [10, -5, 0, -3, 7]
    results = list(map(is_negative, test_cases))
    print(results)