def calculate_rectangle_area(width: int, height: int) -> int:
    if not isinstance(width, int) or not isinstance(height, int):
        raise TypeError("width and height must be integers")
    if width < 0 or height < 0:
        raise ValueError("width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    width = 10
    height = 20
    result = calculate_rectangle_area(width, height)
    print(result)