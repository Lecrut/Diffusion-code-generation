def calculate_rhombus_area(diagonal_a, diagonal_b):
    if diagonal_a <= 0 or diagonal_b <= 0:
        raise ValueError("Diagonals must be positive numbers")
    return (diagonal_a * diagonal_b) / 2

if __name__ == '__main__':
    d1 = 10
    d2 = 20
    area = calculate_rhombus_area(d1, d2)
    print(area)