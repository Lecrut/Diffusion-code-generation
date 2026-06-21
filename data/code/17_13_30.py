def validate_integer(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

def is_even(number):
    validate_integer(number)
    return (number & 1) == 0

if __name__ == '__main__':
    test_values = [2, -3, 4, 7, 8, -9, 0, 15, 16]
    for value in test_values:
        try:
            result = is_even(value)
            print(f"{value} is even: {result}")
        except ValueError as e:
            print(e)