def validate_side_length(side_length):
    if side_length <= 0:
        raise ValueError('Side length must be positive')

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length * side_length

if __name__ == '__main__':
    try:
        print(calculate_square_area(4))
        print(calculate_square_area(-5))
    except ValueError as e:
        print(e)