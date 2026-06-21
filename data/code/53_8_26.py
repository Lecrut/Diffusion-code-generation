def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    try:
        AREA_CONSTANT = 25.0
        side_length = calculate_square_side_length(AREA_CONSTANT)
        print(side_length)
    except ValueError as e:
        print(e)