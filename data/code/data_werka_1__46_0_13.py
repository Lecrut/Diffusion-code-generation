def calculate_triangle_perimeter(a, b, c):
    return a + b + c

if __name__ == '__main__':
    side1 = 6
    side2 = 8
    side3 = 10
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)