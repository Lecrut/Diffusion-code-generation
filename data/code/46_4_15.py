def calculate_triangle_perimeter(sides):
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = {'a': 3, 'b': 4, 'c': 5}
    perimeter = calculate_triangle_perimeter(triangle_sides.values())
    print(perimeter)