def calculate_perimeter(a, b, c):
    return sum([a, b, c])

if __name__ == '__main__':
    side1 = 7
    side2 = 9
    side3 = 11
    triangle_perimeter = calculate_perimeter(side1, side2, side3)
    print(triangle_perimeter)