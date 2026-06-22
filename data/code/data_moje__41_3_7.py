def calculate_rhombus_area(diagonal1, diagonal2):
    if diagonal1 <= 0 or diagonal2 <= 0:
        raise ValueError("Diagonals must be positive numbers")
    return (diagonal1 * diagonal2) / 2

if __name__ == '__main__':
    d1 = 10
    d2 = 20
    area = calculate_rhombus_area(d1, d2)
    print(area)