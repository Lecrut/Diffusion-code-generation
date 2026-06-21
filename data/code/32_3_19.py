def compute_rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numbers.")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    return width * height

if __name__ == '__main__':
    sample_width = 5.0
    sample_height = 10.0
    area = compute_rectangle_area(sample_width, sample_height)
    print(area)