def calculate_triangle_perimeter(side1, side2, side3):
    sides = [side1, side2, side3]
    perimeter = sum(sides)
    return perimeter

if __name__ == '__main__':
    a = 7
    b = 10
    c = 5
    result = calculate_triangle_perimeter(a, b, c)
    print(result)