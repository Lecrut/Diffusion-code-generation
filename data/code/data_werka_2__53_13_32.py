def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    sample_areas = [36, 49, 64]
    for area in sample_areas:
        side_length = calculate_square_side_length(area)
        print(f"The side length of the square with area {area} is: {side_length}")