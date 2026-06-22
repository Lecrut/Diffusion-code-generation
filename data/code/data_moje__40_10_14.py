DIMENSIONS = {
    "length": 10,
    "width": 5,
    "height": 3
}

def calculate_surface_area(dim_dict):
    l = dim_dict["length"]
    w = dim_dict["width"]
    h = dim_dict["height"]
    side_pairs = [(l, w), (w, h), (h, l)]
    total = 0
    for a, b in side_pairs:
        total += a * b
    return total * 2

if __name__ == '__main__':
    area = calculate_surface_area(DIMENSIONS)
    print(area)