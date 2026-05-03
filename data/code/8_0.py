import sys
def calculate_rectangle_area(length, width):
    return length * width
if __name__ == '__main__':
    length = 10.5
    width = 5.0
    area = calculate_rectangle_area(length, width)
    print(area)