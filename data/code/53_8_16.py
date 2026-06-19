def validate_area(area):
    if not isinstance(area, (int, float)):
        raise TypeError("Area must be a number")
    if area < 0:
        raise ValueError("Area cannot be negative")

def find_side_length(area):
    validate_area(area)
    return area ** 0.5

if __name__ == '__main__':
    sample_areas = [16, 49, 81]
    for area in sample_areas:
        try:
            side_length = find_side_length(area)
            print(f"The side length of the square with area {area} is: {side_length}")
        except (TypeError, ValueError) as e:
            print(e)