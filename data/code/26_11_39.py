def is_greater(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    sample_values = [
        (10, 5),
        (3, 7),
        (-1, -5),
        (0, 0),
        (100, 100),
        (-10, -20)
    ]
    
    for num1, num2 in sample_values:
        result = is_greater(num1, num2)
        print(f"Is {num1} greater than {num2}? {result}")