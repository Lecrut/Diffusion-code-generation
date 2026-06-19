def calculate_triangle_perimeter(sides):
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = {'side1': 7, 'side2': 9, 'side3': 12}
    perimeter = calculate_triangle_perimeter(triangle_sides.values())
    print(perimeter)