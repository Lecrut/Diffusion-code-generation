def calculate_area(width: int, height: int) -> int:
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative integers")
    return width * height

if __name__ == '__main__':
    try:
        area = calculate_area(5, 3)
        print(area)
    except ValueError as e:
        print(e)