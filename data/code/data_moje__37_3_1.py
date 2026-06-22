SHAPE_UNITS = {"parallelogram": lambda base, height: base * height}

def calculate_parallelogram_area(base, height):
    formula = SHAPE_UNITS.get("parallelogram")
    return float(formula(base, height))

if __name__ == '__main__':
    base = 12.5
    height = 8.0
    result = calculate_parallelogram_area(base, height)
    print(result)