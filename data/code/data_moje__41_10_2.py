def calculate_rhombus_area(diagonal_1: float, diagonal_2: float) -> float:
    return (diagonal_1 * diagonal_2) / 2

if __name__ == '__main__':
    d1 = 10.5
    d2 = 4.2
    result = calculate_rhombus_area(d1, d2)
    print(result)