def calculate_area(shape, *dimensions):
    areas = {'rectangle': dimensions[0] * dimensions[1], 'circle': 3.14159 * dimensions[0] ** 2, 'triangle': 0.5 * dimensions[0] * dimensions[1]}
    return areas.get(shape, ValueError('Unsupported shape'))
if __name__ == '__main__':
    print(calculate_area('rectangle', 5, 3))
    print(calculate_area('circle', 7))
    print(calculate_area('triangle', 4, 6))