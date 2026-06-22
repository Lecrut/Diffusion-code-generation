def calculate_rhombus_area(diagonal_1, diagonal_2):
    return 0.5 * diagonal_1 * diagonal_2

if __name__ == '__main__':
    d1 = 10
    d2 = 15
    area = calculate_rhombus_area(d1, d2)
    print(area)