def compare(a, b):
    return a > b

if __name__ == '__main__':
    test_cases = {
        'case1': (25, 20),
        'case2': (10, 30),
        'case3': (15, 15)
    }
    for case, values in test_cases.items():
        result = compare(*values)
        print(f"{case}: {result}")