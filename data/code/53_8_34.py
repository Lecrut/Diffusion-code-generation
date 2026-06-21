def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    DEFAULT_AREA = 25.0
    try:
        computed_side_length = calculate_square_side_length(DEFAULT_AREA)
        print(f"The side length of the square is: {computed_side_length}")
    except ValueError as e:
        print(e)