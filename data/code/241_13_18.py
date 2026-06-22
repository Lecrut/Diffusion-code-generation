RECTANGLE_AREA_CONSTANTS = {
    'length': 5,
    'width': 3
}

def calculate_rectangle_area(length, width):
    return length * width

if __name__ == '__main__':
    area = calculate_rectangle_area(RECTANGLE_AREA_CONSTANTS['length'], RECTANGLE_AREA_CONSTANTS['width'])
    print(area)