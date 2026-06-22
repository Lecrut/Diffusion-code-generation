def compare(a, b):
    return a > b

if __name__ == '__main__':
    test_cases = {
        'case1': (25, 20),
        'case2': (5, 10),
        'case3': (7, 7)
    }
    for name, (x, y) in test_cases.items():
        result = compare(x, y)
        print(f"{name}: {result}")