def validate_area(area):
    if not isinstance(area, (int, float)):
        raise ValueError("Area must be a number")
    if area < 0:
        raise ValueError("Area cannot be negative")

def calculate_square_side_length(area):
    validate_area(area)
    return area ** 0.5

if __name__ == '__main__':
    AREA_CONSTANT = 25.0
    try:
        side_length = calculate_square_side_length(AREA_CONSTANT)
        print(side_length)
    except ValueError as e:
        print(e)