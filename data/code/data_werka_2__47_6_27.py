def calculate_area(shape, dimensions):
    return {
        'rectangle': dimensions[0] * dimensions[1],
        'circle': 3.14159 * dimensions[0] ** 2,
        'triangle': 0.5 * dimensions[0] * dimensions[1]
    }.get(shape.lower(), None)

if __name__ == '__main__':
    shape = 'rectangle'
    dimensions = (5, 10)
    area = calculate_area(shape, dimensions)
    print(area)