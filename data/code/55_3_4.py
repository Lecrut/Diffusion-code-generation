def calculate_perimeter(a: float, b: float, c: float) -> float:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    side1 = 5.5
    side2 = 6.6
    side3 = 7.7
    try:
        perimeter = calculate_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)