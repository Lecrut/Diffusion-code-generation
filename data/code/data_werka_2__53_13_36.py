def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    test_areas = [9, 36, 49]
    for area in test_areas:
        try:
            side_length = calculate_square_side_length(area)
            print(f"The side length of the square with area {area} is: {side_length}")
        except ValueError as e:
            print(e)