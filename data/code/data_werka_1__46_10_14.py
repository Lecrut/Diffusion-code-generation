def calculate_triangle_perimeter(a, b, c):
    return a + b + c

if __name__ == '__main__':
    side1 = 7.0
    side2 = 8.5
    side3 = 9.2
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)