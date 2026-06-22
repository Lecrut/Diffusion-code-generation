RECTANGLE_WIDTH = 7
RECTANGLE_HEIGHT = 11

def compute_rectangle_area(width, height):
    return width * height

if __name__ == '__main__':
    area = compute_rectangle_area(RECTANGLE_WIDTH, RECTANGLE_HEIGHT)
    print(area)