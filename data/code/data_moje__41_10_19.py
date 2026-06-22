def calculate_rhombus_area(diagonal1: float, diagonal2: float) -> float:
    product = diagonal1 * diagonal2
    return product / 2.0

if __name__ == '__main__':
    sample_d1 = 12.5
    sample_d2 = 4.0
    computed_area = calculate_rhombus_area(sample_d1, sample_d2)
    print(computed_area)