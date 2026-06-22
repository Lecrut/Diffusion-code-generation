def area_of_rhombus(diagonal1: float, diagonal2: float) -> float:
    return (diagonal1 * diagonal2) / 2

if __name__ == '__main__':
    result = area_of_rhombus(10.0, 8.0)
    print(result)