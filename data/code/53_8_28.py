def validate_area(area):
    if not isinstance(area, (int, float)):
        raise TypeError("Area must be a number")
    if area < 0:
        raise ValueError("Area cannot be negative")

def calculate_square_side_length(area):
    validate_area(area)
    return area ** 0.5

if __name__ == '__main__':
    HARD_CODED_AREA = 25.0
    try:
        side_length = calculate_square_side_length(HARD_CODED_AREA)
        print(side_length)
    except (TypeError, ValueError) as e:
        print(e)