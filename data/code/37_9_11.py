def calculate_parallelogram_area(base: float, height: float) -> float:
    return base * height

if __name__ == '__main__':
    sample_base = 10.0
    sample_height = 5.0
    area = calculate_parallelogram_area(sample_base, sample_height)
    print(area)