RECTANGLE_ATTRIBUTES = {
    "length": 25,
    "width": 15
}

def compute_area(attributes):
    length = attributes["length"]
    width = attributes["width"]
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

if __name__ == '__main__':
    try:
        area = compute_area(RECTANGLE_ATTRIBUTES)
        print(area)
    except ValueError as e:
        print(e)