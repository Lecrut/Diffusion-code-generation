def is_greater(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return num1 > num2

if __name__ == '__main__':
    sample_values = [
        (15, 10),
        (5, 8),
        (-3, -6),
        (0, 0),
        (1.5, 1.5),
        (2.5, 2)
    ]
    for num1, num2 in sample_values:
        result = is_greater(num1, num2)
        print(f"is_greater({num1}, {num2}) = {result}")