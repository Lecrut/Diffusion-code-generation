RECTANGLE_DIMENSIONS = {
    "length": 12,
    "width": 8
}

def calculate_area(dimensions):
    return dimensions["length"] * dimensions["width"]

if __name__ == '__main__':
    area = calculate_area(RECTANGLE_DIMENSIONS)
    print(area)