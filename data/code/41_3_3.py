def calculate_rhombus_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

if __name__ == '__main__':
    d1 = 6
    d2 = 8
    area = calculate_rhombus_area(d1, d2)
    print(area)