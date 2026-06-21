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
    results = [is_greater(num1, num2) for num1, num2 in test_cases]
    for i, result in enumerate(results):
        print(f"Test case {i+1}: is_greater{test_cases[i]} = {result}")