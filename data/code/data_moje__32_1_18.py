def compute_rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numeric.")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    return float(width) * float(height)

if __name__ == '__main__':
    width_value = 7.5
    height_value = 4.2
    area_result = compute_rectangle_area(width_value, height_value)
    print(area_result)