def calculate_area(shape, *dimensions):
    area = {'rectangle': dimensions[0] * dimensions[1], 'circle': 3.14159 * dimensions[0] ** 2, 'triangle': 0.5 * dimensions[0] * dimensions[1]}.get(shape)
    if area is None:
        raise ValueError(f'Unsupported shape: {shape}')
    return area
if __name__ == '__main__':
    print(calculate_area('rectangle', 3, 4))
    print(calculate_area('circle', 5))
    print(calculate_area('triangle', 6, 7))