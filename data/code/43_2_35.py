def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a numeric value.")

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length * side_length

if __name__ == '__main__':
    try:
        print(calculate_square_area(4))
        print(calculate_square_area(8.2))
        print(calculate_square_area('invalid'))
    except ValueError as e:
        print(e)