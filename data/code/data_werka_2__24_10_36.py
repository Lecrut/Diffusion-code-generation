NEGATIVE_THRESHOLD = 0

is_negative = lambda x: x < NEGATIVE_THRESHOLD

if __name__ == '__main__':
    test_cases = [-10, 0, 5, -1, 1, -10, 15]
    results = {x: is_negative(x) for x in test_cases}
    print(results)