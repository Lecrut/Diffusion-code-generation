def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError('Width must be a number')
    if not isinstance(height, (int, float)):
        raise TypeError('Height must be a number')
    if width < 0:
        raise ValueError('Width cannot be negative')
    if height < 0:
        raise ValueError('Height cannot be negative')
    return width * height
if __name__ == '__main__':
    sample_width = 5.0
    sample_height = 10.0
    area = calculate_rectangle_area(sample_width, sample_height)
    print(area)