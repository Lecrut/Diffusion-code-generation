def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numbers")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height

def parse_dimension(value):
    try:
        dimension = float(value)
        if dimension < 0:
            raise ValueError
        return dimension
    except (ValueError, TypeError):
        raise ValueError(f"Invalid dimension: {value}")

if __name__ == '__main__':
    sample_width = 5.0
    sample_height = 10.0
    area = calculate_rectangle_area(sample_width, sample_height)
    print(area)