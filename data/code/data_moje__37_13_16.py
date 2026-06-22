def calculate_parallelogram_area(base: float, height: float) -> float:
    return base * height

if __name__ == '__main__':
    base_value = 10.5
    height_value = 7.2
    area_result = calculate_parallelogram_area(base_value, height_value)
    print(area_result)