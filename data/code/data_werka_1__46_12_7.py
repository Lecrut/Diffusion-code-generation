def calculate_perimeter(a, b, c):
    return a + b + c

if __name__ == '__main__':
    triangle_sides = {'a': 3.0, 'b': 4.0, 'c': 5.0}
    perimeter = calculate_perimeter(triangle_sides['a'], triangle_sides['b'], triangle_sides['c'])
    print(perimeter)