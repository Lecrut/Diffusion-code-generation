def calculate_rectangle_area(width: int, height: int) -> int:
    if not isinstance(width, int) or not isinstance(height, int):
        raise TypeError("Width and height must be integers")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    sample_width = 10
    sample_height = 5
    result = calculate_rectangle_area(sample_width, sample_height)
    print(result)