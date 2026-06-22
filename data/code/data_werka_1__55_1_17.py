def calculate_perimeter(sides):
    return sum(sides.values())

if __name__ == '__main__':
    triangle_sides = {'side1': 3.0, 'side2': 4.0, 'side3': 5.0}
    print(calculate_perimeter(triangle_sides))