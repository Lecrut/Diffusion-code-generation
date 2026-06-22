def is_strictly_greater(num1, num2):
    return num1 > num2

def validate_input(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Invalid input: {value} is not an integer.")

if __name__ == '__main__':
    sample_values = [
        (5, 3),
        (10, 10),
        (-1, -2),
        ('a', 3),
        (7, 'b')
    ]

    for value1, value2 in sample_values:
        try:
            num1 = validate_input(value1)
            num2 = validate_input(value2)
            result = is_strictly_greater(num1, num2)
            print(result)
        except ValueError as e:
            print(e)