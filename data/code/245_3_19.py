def calculate_area(width, height):
    return width * height

def compare_areas(rect1, rect2):
    area1 = calculate_area(*rect1)
    area2 = calculate_area(*rect2)
    return area1 == area2

if __name__ == '__main__':
    rectangle1 = (3.0, 4.0)
    rectangle2 = (6.0, 2.0)
    result = compare_areas(rectangle1, rectangle2)
    print(f"Rectangle areas are equal: {result}")