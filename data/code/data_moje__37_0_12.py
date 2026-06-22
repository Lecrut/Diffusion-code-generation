def calculate_parallelogram_area(base, height):
    shape_metrics = {
        "parallelogram": {
            "area_formula": lambda b, h: b * h
        }
    }
    return shape_metrics["parallelogram"]["area_formula"](base, height)

if __name__ == '__main__':
    b = 10.0
    h = 4.5
    area = calculate_parallelogram_area(b, h)
    print(area)