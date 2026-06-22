def calculate_rhombus_area(d1, d2):
    if d1 <= 0 or d2 <= 0:
        raise ValueError("Diagonal lengths must be positive numbers.")
    return (d1 * d2) / 2

if __name__ == '__main__':
    diagonal_a = 10
    diagonal_b = 8
    area = calculate_rhombus_area(diagonal_a, diagonal_b)
    print(area)