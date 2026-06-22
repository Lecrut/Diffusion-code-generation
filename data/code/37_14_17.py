def compute_parallelogram_area(base: int, height: int) -> int:
    return base * height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    area = compute_parallelogram_area(sample_base, sample_height)
    print(area)