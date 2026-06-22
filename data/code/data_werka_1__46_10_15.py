def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        return None
    return a + b + c

if __name__ == '__main__':
    side1 = 7.5
    side2 = 9.3
    side3 = 4.8
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    if perimeter is not None:
        print(perimeter)