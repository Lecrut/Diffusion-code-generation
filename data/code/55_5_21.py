def calculate_perimeter(sides):
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = {'side1': 3, 'side2': 4, 'side3': 5}
    perimeter = calculate_perimeter(triangle_sides.values())
    print(perimeter)