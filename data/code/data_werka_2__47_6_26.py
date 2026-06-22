if __name__ == '__main__':
    shapes = [
        {'type': 'circle', 'radius': 5},
        {'type': 'rectangle', 'length': 4, 'width': 6},
        {'type': 'triangle', 'base': 3, 'height': 7}
    ]
    for shape in shapes:
        print(calculate_area(shape))