def calculate_triangle_perimeter(a, b, c):
    return a + b + c

if __name__ == '__main__':
    SIDES = [7, 24, 25]
    if all(side > 0 for side in SIDES):
        perimeter = calculate_triangle_perimeter(*SIDES)
        print(perimeter)