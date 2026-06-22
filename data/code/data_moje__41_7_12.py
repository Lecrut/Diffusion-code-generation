import math

def calculate_rhombus_area(diagonal_a, diagonal_b):
    if diagonal_a <= 0 or diagonal_b <= 0:
        raise ValueError("Diagonals must be positive numbers.")
    if not math.isfinite(diagonal_a) or not math.isfinite(diagonal_b):
        raise ValueError("Diagonals must be finite numbers.")
    return (diagonal_a * diagonal_b) / 2.0

if __name__ == '__main__':
    d1 = 10.0
    d2 = 12.0
    result = calculate_rhombus_area(d1, d2)
    print(result)