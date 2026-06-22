def is_valid_area(area):
    return area >= 0

def find_side_length(area):
    if not is_valid_area(area):
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    sample_areas = [16, 49, 81]
    for area in sample_areas:
        try:
            side_length = find_side_length(area)
            print(f"The side length of the square with area {area} is: {side_length}")
        except ValueError as e:
            print(e)