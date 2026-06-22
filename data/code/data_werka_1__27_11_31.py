def compare_values(value1, value2):
    return abs(value1 - value2) > 1e-10

if __name__ == '__main__':
    test_cases = {
        'case1': (10, 10.00000000000001),
        'case2': (5, 5.000000000000001),
        'case3': (3.14159, 3.14159000000001)
    }
    
    for name, (a, b) in test_cases.items():
        result = compare_values(a, b)
        print(f'{name}: {result}')