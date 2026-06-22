RECTANGLE_DIMENSIONS = {
    "width": 7,
    "height": 4
}

def calculate_perimeter(dimensions):
    width = dimensions["width"]
    height = dimensions["height"]
    return 2 * (width + height)

if __name__ == '__main__':
    perimeter = calculate_perimeter(RECTANGLE_DIMENSIONS)
    print(perimeter)