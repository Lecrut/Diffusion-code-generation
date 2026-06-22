def validate_numbers(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both x and y must be numbers")

is_greater = lambda x, y: x > y

if __name__ == '__main__':
    try:
        validate_numbers(25, 10)
        print(is_greater(25, 10))
        
        validate_numbers(8, 15)
        print(is_greater(8, 15))
    except ValueError as e:
        print(e)