def calculate_rhombus_area(diagonal_one: float, diagonal_two: float) -> float:
    if diagonal_one <= 0 or diagonal_two <= 0:
        raise ValueError("Diagonals must be positive numbers")
    return (diagonal_one * diagonal_two) / 2

if __name__ == '__main__':
    d1 = 10.0
    d2 = 8.0
    area = calculate_rhombus_area(d1, d2)
    print(area)