def calculate_area(length: int, width: int) -> int:
    return length * width

if __name__ == '__main__':
    rect_length = 7
    rect_width = 4
    area = calculate_area(rect_length, rect_width)
    print(area)