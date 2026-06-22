SHAPES = {
    "kite": 2,
}

def calculate_perimeter(shape_type, *dimensions):
    if shape_type not in SHAPES:
        return 0
    num_sides = SHAPES[shape_type]
    if len(dimensions) != num_sides:
        return 0
    return sum(dimensions)

if __name__ == '__main__':
    print(calculate_perimeter("kite", 5, 7))