def area_of_rhombus(diagonal1: float, diagonal2: float) -> float:
    return diagonal1 * diagonal2 / 2.0

if __name__ == '__main__':
    d1: float = 10.0
    d2: float = 8.0
    area: float = area_of_rhombus(d1, d2)
    print(area)