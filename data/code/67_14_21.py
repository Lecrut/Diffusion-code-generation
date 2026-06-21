def add_numbers(a, b):
    return a + b

if __name__ == '__main__':
    sample_values = {
        'case1': (5, 3),
        'case2': (2.5, 4.7),
        'case3': (-1, -1),
        'case4': (0, 0),
        'case5': (100, 200.5)
    }
    
    for key, (num1, num2) in sample_values.items():
        result = add_numbers(num1, num2)
        print(f"Result of adding {num1} and {num2}: {result}")