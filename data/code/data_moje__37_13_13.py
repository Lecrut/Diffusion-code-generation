def parallelogram_area(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return base * height

if __name__ == '__main__':
    base_val = 10.0
    height_val = 5.0
    area = parallelogram_area(base_val, height_val)
    print(area)