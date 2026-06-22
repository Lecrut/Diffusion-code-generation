import math

def calculate_rhombus_area(diagonal1: float, diagonal2: float) -> float:
    area = (diagonal1 * diagonal2) / 2
    return area

if __name__ == '__main__':
    diagonal_1 = 10
    diagonal_2 = 8
    result = calculate_rhombus_area(diagonal_1, diagonal_2)
    print(result)