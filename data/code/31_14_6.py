def is_valid_side(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side must be a number")
    if side < 0:
        raise ValueError("Side must be non-negative")
    return True

def calculate_square_area(side_length):
    is_valid_side(side_length)
    return side_length * side_length

if __name__ == '__main__':
    fixed_side = 50
    computed_area = calculate_square_area(fixed_side)
    print(computed_area)