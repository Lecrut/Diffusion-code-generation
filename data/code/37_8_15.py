UNIT_FACTORS = {"cm": 1, "m": 1, "in": 1, "ft": 1}

def calculate_parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    dimensions = {"base": 7, "height": 4}
    area = calculate_parallelogram_area(dimensions["base"], dimensions["height"])
    print(area)