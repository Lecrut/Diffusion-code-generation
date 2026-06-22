def calculate_rhombus_area(d1, d2):
    return (d1 * d2) / 2

if __name__ == '__main__':
    diagonal1 = 10
    diagonal2 = 15
    area = calculate_rhombus_area(diagonal1, diagonal2)
    print(area)