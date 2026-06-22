def calculate_rhombus_area(diagonal_one: float, diagonal_two: float) -> float:
    return (diagonal_one * diagonal_two) / 2

if __name__ == '__main__':
    d1 = 10.0
    d2 = 15.0
    print(calculate_rhombus_area(d1, d2))