def compute_parallelogram_area(base: float, height: float) -> float:
    return base * height

if __name__ == '__main__':
    base_value = 10.0
    height_value = 5.0
    area = compute_parallelogram_area(base_value, height_value)
    print(area)