def calculate_rectangle_area(width: int, height: int) -> int:
    if not isinstance(width, int):
        raise TypeError("width must be an integer")
    if not isinstance(height, int):
        raise TypeError("height must be an integer")
    if width < 0 or height < 0:
        raise ValueError("width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    sample_width = 10
    sample_height = 5
    area = calculate_rectangle_area(sample_width, sample_height)
    print(area)