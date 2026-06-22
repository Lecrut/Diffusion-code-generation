SHAPE_DIMENSIONS = {'rectangle': (10, 5)}

def calculate_area(shape):
    length, width = SHAPE_DIMENSIONS.get(shape, (0, 0))
    return length * width
if __name__ == '__main__':
    area = calculate_area('rectangle')
    print(area)