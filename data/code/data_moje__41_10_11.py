def calculate_rhombus_area(diagonal1: float, diagonal2: float) -> float:
    return (diagonal1 * diagonal2) / 2

if __name__ == '__main__':
    sample_d1 = 5.0
    sample_d2 = 8.0
    result = calculate_rhombus_area(sample_d1, sample_d2)
    print(result)