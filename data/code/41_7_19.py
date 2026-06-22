import math

def calculate_rhombus_area(diagonal_1, diagonal_2):
    if diagonal_1 <= 0 or diagonal_2 <= 0:
        raise ValueError("Diagonals must be positive values")
    if not (math.isfinite(diagonal_1) and math.isfinite(diagonal_2)):
        raise ValueError("Diagonals must be finite numbers")
    return (diagonal_1 * diagonal_2) / 2.0

if __name__ == "__main__":
    d1 = 10.5
    d2 = 7.2
    area = calculate_rhombus_area(d1, d2)
    print(area)