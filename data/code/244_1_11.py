WIDTH = 10
HEIGHT = 6
BASE = 8
HEIGHT_T = 5

def calculate_area():
    rectangle_area = WIDTH * HEIGHT
    triangle_area = 0.5 * BASE * HEIGHT_T
    total_area = rectangle_area + triangle_area
    return total_area

if __name__ == '__main__':
    result = calculate_area()
    print(result)