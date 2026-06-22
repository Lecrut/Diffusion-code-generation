def compute_rhombus_area(diagonal1: float, diagonal2: float) -> float:
    return (diagonal1 * diagonal2) / 2

if __name__ == '__main__':
    diagonal1 = 10
    diagonal2 = 5
    result = compute_rhombus_area(diagonal1, diagonal2)
    print(result)