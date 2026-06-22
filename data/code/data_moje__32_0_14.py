def calculate_rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    width_value = 5
    height_value = 10
    area_result = calculate_rectangle_area(width_value, height_value)
    print(area_result)