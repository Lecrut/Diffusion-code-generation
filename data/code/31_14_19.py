def validate_side_length(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Side length must be a number")
    if value <= 0:
        raise ValueError("Side length must be positive")
    return True

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length ** 2

if __name__ == '__main__':
    SIDE = 50
    computed_area = calculate_square_area(SIDE)
    print(computed_area)