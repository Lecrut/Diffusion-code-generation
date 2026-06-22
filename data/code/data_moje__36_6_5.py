def trapezoid_area(b1: float, b2: float, h: float) -> float:
    return (b1 + b2) * h / 2

if __name__ == '__main__':
    result = trapezoid_area(10, 20, 5)
    print(result)