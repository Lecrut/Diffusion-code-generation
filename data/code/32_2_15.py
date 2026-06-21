def calculate_rectangle_area(width: float, height: float) -> float:
    area_value = width * height
    return area_value

if __name__ == '__main__':
    rect_width = 7.5
    rect_height = 4.2
    computed_area = calculate_rectangle_area(rect_width, rect_height)
    print(computed_area)