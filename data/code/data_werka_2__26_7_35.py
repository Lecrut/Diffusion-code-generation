def validate_input(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both x and y must be integers or floats")

is_greater = lambda x, y: x > y

if __name__ == '__main__':
    try:
        validate_input(10, 5)
        print(is_greater(10, 5))
        
        validate_input(3, 7)
        print(is_greater(3, 7))
    except ValueError as e:
        print(e)