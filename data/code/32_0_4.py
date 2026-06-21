def calculate_rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    return width * height

if __name__ == "__main__":
    sample_width = 10
    sample_height = 5
    area = calculate_rectangle_area(sample_width, sample_height)
    print(area)