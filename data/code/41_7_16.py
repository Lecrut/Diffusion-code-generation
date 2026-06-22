import math

def calculate_rhombus_area(diagonal_1, diagonal_2):
    if diagonal_1 <= 0 or diagonal_2 <= 0:
        raise ValueError("Diagonals must be positive numbers")
    return 0.5 * diagonal_1 * diagonal_2

if __name__ == '__main__':
    d1 = 10.0
    d2 = 14.0
    area = calculate_rhombus_area(d1, d2)
    print(area)