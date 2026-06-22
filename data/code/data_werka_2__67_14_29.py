def add_numbers(a, b):
    return a + b

if __name__ == '__main__':
    test_cases = {
        'case1': (5, 3),
        'case2': (2.5, 4.7),
        'case3': (-10, 20),
        'case4': (0, 0),
        'case5': (100.5, 200)
    }
    
    for label, (num1, num2) in test_cases.items():
        result = add_numbers(num1, num2)
        print(f"Test case {label}: {result}")