def is_greater(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    test_values = {
        'case1': (10, 5),
        'case2': (3, 7),
        'case3': (-1, -5),
        'case4': (0, 0),
        'case5': (100, 100),
        'case6': (-10, -20)
    }
    
    for case, (num1, num2) in test_values.items():
        result = is_greater(num1, num2)
        print(f"{case}: is_greater({num1}, {num2}) = {result}")