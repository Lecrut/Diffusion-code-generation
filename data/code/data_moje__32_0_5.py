def calculate_rectangle_area(width, height):
    if width < 0:
        raise ValueError("Width must be non-negative")
    if height < 0:
        raise ValueError("Height must be non-negative")
    return width * height

if __name__ == '__main__':
    sample_width = 5
    sample_height = 10
    area = calculate_rectangle_area(sample_width, sample_height)
    print(area)