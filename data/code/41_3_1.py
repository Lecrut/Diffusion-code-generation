def calculate_rhombus_area(d1, d2):
    return (d1 * d2) / 2

if __name__ == '__main__':
    diagonal_1 = 10
    diagonal_2 = 8
    area = calculate_rhombus_area(diagonal_1, diagonal_2)
    print(area)