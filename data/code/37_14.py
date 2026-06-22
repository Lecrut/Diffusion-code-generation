def compute_parallelogram_area(base: float, height: float) -> float:
    return base * height

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    area = compute_parallelogram_area(base_value, height_value)
    print(area)