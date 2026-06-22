def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    test_areas = [16, 25, 81]
    for area in test_areas:
        side_length = calculate_square_side_length(area)
        print(side_length)