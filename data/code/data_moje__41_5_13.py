def calculate_rhombus_area(d1, d2):
    return (d1 * d2) / 2

if __name__ == '__main__':
    diagonal_one = 10
    diagonal_two = 8
    area = calculate_rhombus_area(diagonal_one, diagonal_two)
    print(area)