def _validate_dimensions(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Dimensions must be numeric")
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return True

def compute_rectangle_area(width, height):
    _validate_dimensions(width, height)
    return width * height

if __name__ == '__main__':
    sample_width = 4
    sample_height = 6
    area_result = compute_rectangle_area(sample_width, sample_height)
    print(area_result)