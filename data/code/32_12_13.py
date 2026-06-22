def _validate_dimensions(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be numeric")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be numeric")
    if width < 0:
        raise ValueError("Width must be non-negative")
    if height < 0:
        raise ValueError("Height must be non-negative")
    return True

def compute_rectangle_area(width, height):
    _validate_dimensions(width, height)
    return width * height

if __name__ == '__main__':
    sample_width = 6.0
    sample_height = 4.0
    area_result = compute_rectangle_area(sample_width, sample_height)
    print(area_result)