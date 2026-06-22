def calculate_area(x1, y1, x2, y2, x3, y3):

    def is_valid_coordinate(coord):
        return isinstance(coord, (int, float)) and coord >= 0
    if not all((is_valid_coordinate(coord) for coord in [x1, y1, x2, y2, x3, y3])):
        raise ValueError('Invalid coordinate values')
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
if __name__ == '__main__':
    print(calculate_area(0, 0, 4, 0, 0, 3))