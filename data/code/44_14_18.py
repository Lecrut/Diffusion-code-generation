RECTANGLE_PROPERTIES = {
    "width": 9,
    "height": 2
}

def calculate_perimeter(properties):
    width = properties["width"]
    height = properties["height"]
    return 2 * (width + height)

if __name__ == '__main__':
    perimeter = calculate_perimeter(RECTANGLE_PROPERTIES)
    print(perimeter)