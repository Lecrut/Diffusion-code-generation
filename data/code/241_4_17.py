def validate_dimensions(width: int, height: int) -> None:
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers")

def calculate_area(width: int, height: int) -> int:
    return width * height

if __name__ == '__main__':
    try:
        validate_dimensions(5, 3)
        area = calculate_area(5, 3)
        print(area)
    except ValueError as e:
        print(e)