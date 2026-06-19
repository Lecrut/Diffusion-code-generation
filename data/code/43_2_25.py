def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a numeric value.")
    return side_length * side_length

if __name__ == '__main__':
    try:
        sample_side_length = 5
        area = calculate_square_area(sample_side_length)
        print(area)
    except ValueError as e:
        print(e)