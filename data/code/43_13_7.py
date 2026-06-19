def calculate_square_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return side_length * side_length

if __name__ == '__main__':
    try:
        sample_side_length = 6
        area = calculate_square_area(sample_side_length)
        print(area)
    except ValueError as e:
        print(e)