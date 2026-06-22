def calculate_rectangle_area(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return length * width
    else:
        return None

if __name__ == '__main__':
    print(calculate_rectangle_area(5, 3))
    print(calculate_rectangle_area(7.5, 2.4))
    print(calculate_rectangle_area('a', 3))