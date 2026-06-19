def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a numeric value.")
    return side_length * side_length

if __name__ == '__main__':
    try:
        print(calculate_square_area(8))
        print(calculate_square_area(12.3))
        print(calculate_square_area('b'))
    except ValueError as e:
        print(e)