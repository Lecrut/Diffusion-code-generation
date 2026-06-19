def calculate_area(base, height):
    shape_type = "triangle"
    area_calculators = {
        "triangle": lambda b, h: 0.5 * b * h,
        "rectangle": lambda l, w: l * w
    }
    calculator = area_calculators.get(shape_type)
    if not calculator:
        raise ValueError("Unsupported shape type")
    return calculator(base, height)

if __name__ == '__main__':
    base_sample = 7.5
    height_sample = 4.0
    result = calculate_area(base_sample, height_sample)
    print(result)