def is_greater(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return num1 > num2

if __name__ == '__main__':
    sample_values = [
        (10, 5),
        (3, 7),
        (-1, -5),
        (0, 0),
        (100.5, 100),
        (-20, -10)
    ]
    for num1, num2 in sample_values:
        try:
            result = is_greater(num1, num2)
            print(f"is_greater({num1}, {num2}) = {result}")
        except ValueError as e:
            print(e)