def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("width must be a numeric value")
    if not isinstance(height, (int, float)):
        raise TypeError("height must be a numeric value")
    return width * height

if __name__ == '__main__':
    sample_width = 5
    sample_height = 10
    result = calculate_rectangle_area(sample_width, sample_height)
    print(result)