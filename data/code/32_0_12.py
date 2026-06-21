def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numbers")
    if width < 0:
        raise ValueError(f"Width cannot be negative: {width}")
    if height < 0:
        raise ValueError(f"Height cannot be negative: {height}")
    return width * height

if __name__ == '__main__':
    w = 7.5
    h = 4
    print(calculate_rectangle_area(w, h))