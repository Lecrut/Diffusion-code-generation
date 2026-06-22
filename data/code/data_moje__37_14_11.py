def calculate_parallelogram_area(base: int, height: int) -> int:
    return base * height

if __name__ == '__main__':
    sample_base = 15
    sample_height = 8
    area = calculate_parallelogram_area(sample_base, sample_height)
    print(area)