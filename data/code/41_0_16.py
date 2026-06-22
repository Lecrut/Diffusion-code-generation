import math

def calculate_rhombus_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

if __name__ == '__main__':
    diag1 = 10
    diag2 = 8
    area = calculate_rhombus_area(diag1, diag2)
    print(area)