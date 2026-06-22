def calculate_rectangle_area(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return float(length * width)
    else:
        return None
if __name__ == '__main__':
    length = 5
    width = 3
    area = calculate_rectangle_area(length, width)
    print(area)