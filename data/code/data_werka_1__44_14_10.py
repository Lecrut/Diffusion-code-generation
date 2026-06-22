RECTANGLE_CONFIG = {
    "dimensions": {
        "width": 9,
        "height": 2
    }
}

def compute_perimeter(config):
    width = config["dimensions"]["width"]
    height = config["dimensions"]["height"]
    return 2 * (width + height)

if __name__ == '__main__':
    perimeter = compute_perimeter(RECTANGLE_CONFIG)
    print(perimeter)