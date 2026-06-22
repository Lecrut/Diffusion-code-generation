def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    return side_length * side_length

if __name__ == '__main__':
    sample_side = 7
    area = calculate_square_area(sample_side)
    print(area)