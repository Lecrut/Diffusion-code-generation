def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

def calculate_perimeter(a: float, b: float, c: float) -> float:
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid triangle sides")
    return a + b + c

if __name__ == '__main__':
    side1 = 7.0
    side2 = 10.0
    side3 = 5.0
    try:
        perimeter = calculate_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)