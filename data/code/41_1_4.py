def compute_rhombus_area(d1: float, d2: float) -> float:
    return 0.5 * d1 * d2

if __name__ == '__main__':
    sample_d1 = 6.0
    sample_d2 = 8.0
    area = compute_rhombus_area(sample_d1, sample_d2)
    print(area)