SQUARE_SIDES = 4

def calculate_square_perimeter(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return SQUARE_SIDES * side_length

if __name__ == '__main__':
    sample_side_length = 9
    try:
        perimeter = calculate_square_perimeter(sample_side_length)
        print(perimeter)
    except ValueError as e:
        print(e)