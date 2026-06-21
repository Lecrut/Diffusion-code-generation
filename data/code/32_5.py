def calculate_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numeric.")
    return width * height

if __name__ == '__main__':
    width_val = 5
    height_val = 10
    result = calculate_area(width_val, height_val)
    print(result)