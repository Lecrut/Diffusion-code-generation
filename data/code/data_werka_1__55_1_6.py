def calculate_perimeter(sides):
    return sum(sides.values())

if __name__ == '__main__':
    triangle_sides = {'a': 3.0, 'b': 4.0, 'c': 5.0}
    print(calculate_perimeter(triangle_sides))