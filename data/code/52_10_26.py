RECTANGLE_LENGTH = 25
RECTANGLE_WIDTH = 15

def compute_area(length, width):
    return length * width

if __name__ == '__main__':
    area = compute_area(RECTANGLE_LENGTH, RECTANGLE_WIDTH)
    print(area)