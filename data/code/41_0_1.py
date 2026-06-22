def calculate_rhombus_area(diagonal1, diagonal2):
    return diagonal1 * diagonal2 / 2
if __name__ == '__main__':
    diagonal1 = 6
    diagonal2 = 8
    area = calculate_rhombus_area(diagonal1, diagonal2)
    print(area)