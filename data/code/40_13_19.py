DIMENSIONS = {"length": 4, "width": 6, "height": 8}

def calculate_surface_area():
    l, w, h = DIMENSIONS["length"], DIMENSIONS["width"], DIMENSIONS["height"]
    return 2 * (l * w + w * h + h * l)

if __name__ == '__main__':
    print(calculate_surface_area())