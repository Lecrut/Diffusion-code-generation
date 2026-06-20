calculate_diff = lambda a, b: abs(a - b)

if __name__ == '__main__':
    test_cases = {
        (10, -5): 15,
        (-15, 7): 22,
        (-100, -50): 50,
        (20, 20): 0
    }
    
    for (num1, num2), expected in test_cases.items():
        result = calculate_diff(num1, num2)
        print(f"Difference between {num1} and {num2}: {result}")