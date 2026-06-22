def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    EXAMPLE_AREA = 36.0
    side_length = calculate_square_side_length(EXAMPLE_AREA)
    print(side_length)