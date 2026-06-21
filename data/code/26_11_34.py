def is_greater(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    test_cases = [
        (10, 5),
        (3, 7),
        (-1, -5),
        (0, 0),
        (100, 100),
        (-10, -20)
    ]
    
    for num1, num2 in test_cases:
        result = is_greater(num1, num2)
        print(f"is_greater({num1}, {num2}) = {result}")