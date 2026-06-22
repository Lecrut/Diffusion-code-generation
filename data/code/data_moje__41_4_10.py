def calculate_rhombus_area(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

if __name__ == '__main__':
    diagonal_a = 10
    diagonal_b = 8
    area = calculate_rhombus_area(diagonal_a, diagonal_b)
    print(area)