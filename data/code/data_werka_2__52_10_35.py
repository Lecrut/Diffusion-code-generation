RECTANGLE_CONFIG = {
    "length": 18,
    "width": 6
}

def compute_area(config):
    return config["length"] * config["width"]

if __name__ == '__main__':
    area = compute_area(RECTANGLE_CONFIG)
    print(area)