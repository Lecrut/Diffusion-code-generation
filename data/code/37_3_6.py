GEOMETRY_FORMULA = lambda base, height: base * height

def calculate_parallelogram_area(base, height):
    return float(GEOMETRY_FORMULA(base, height))

if __name__ == '__main__':
    BASE = 12.5
    HEIGHT = 8.0
    result = calculate_parallelogram_area(BASE, HEIGHT)
    print(result)