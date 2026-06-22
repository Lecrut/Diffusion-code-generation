SHAPE_CONFIGS = {"parallelogram": {"label": "Parallelogram", "calc": lambda b, h: b * h}}

def compute_parallelogram_area(base: float, height: float) -> float:
    return SHAPE_CONFIGS["parallelogram"]["calc"](base, height)

if __name__ == '__main__':
    base_val = 12.0
    height_val = 8.5
    area_result = compute_parallelogram_area(base_val, height_val)
    print(area_result)