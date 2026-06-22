def calculate_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Width and height must be numbers")
    return width * height

if __name__ == '__main__':
    sample_width = 5
    sample_height = 3
    try:
        area = calculate_area(sample_width, sample_height)
        print(area)
    except ValueError as e:
        print(e)