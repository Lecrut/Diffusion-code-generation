def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive integers.")
    return a + b + c

if __name__ == '__main__':
    side1 = 7
    side2 = 9
    side3 = 12
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)