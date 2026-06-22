def calculate_perimeter(a: float, b: float, c: float) -> float:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive")
    return a + b + c

if __name__ == '__main__':
    side1 = 3.5
    side2 = 4.2
    side3 = 5.8
    perimeter = calculate_perimeter(side1, side2, side3)
    print(perimeter)