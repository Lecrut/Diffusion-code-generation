def rhombus_area(d1: float, d2: float) -> float:
    if d1 <= 0 or d2 <= 0:
        raise ValueError('Diagonals must be positive numbers.')
    return d1 * d2 / 2.0
if __name__ == '__main__':
    d1 = 10.0
    d2 = 8.0
    result = rhombus_area(d1, d2)
    print(result)