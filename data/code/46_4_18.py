def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

if __name__ == '__main__':
    a = 3
    b = 4
    c = 5
    perimeter = calculate_triangle_perimeter(a, b, c)
    print(perimeter)