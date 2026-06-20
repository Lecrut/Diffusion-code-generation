def calculate_rectangle_area(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive.")
    return width * height

if __name__ == '__main__':
    width_value = 5.0
    height_value = 10.0
    result = calculate_rectangle_area(width_value, height_value)
    print(result)