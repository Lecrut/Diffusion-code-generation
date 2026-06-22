def calculate_area(width: float, height: float) -> float:
    return width * height

def compare_areas(rect1_width: float, rect1_height: float, rect2_width: float, rect2_height: float) -> bool:
    area1 = calculate_area(rect1_width, rect1_height)
    area2 = calculate_area(rect2_width, rect2_height)
    return area1 == area2

if __name__ == '__main__':
    rectangle1 = (3.0, 4.0)
    rectangle2 = (6.0, 2.0)
    result = compare_areas(*rectangle1, *rectangle2)
    print(f"Areas of rectangles are equal: {result}")