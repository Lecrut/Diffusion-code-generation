is_negative = lambda x: x < 0

if __name__ == '__main__':
    test_values = [10, -5, 0, -1, 23]
    results = list(map(is_negative, test_values))
    print(results)