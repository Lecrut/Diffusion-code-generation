RECTANGLE_CONFIG = {
    "width": 12,
    "height": 8
}

def compute_perimeter(config):
    width = config["width"]
    height = config["height"]
    return 2 * (width + height)

if __name__ == '__main__':
    perimeter_value = compute_perimeter(RECTANGLE_CONFIG)
    print(perimeter_value)