def calculate_rhombus_area(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

if __name__ == '__main__':
    d1 = 10
    d2 = 8
    area = calculate_rhombus_area(d1, d2)
    print(area)