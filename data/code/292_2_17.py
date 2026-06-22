def calculate_triangle_perimeter(a, b, c):
    s = (a + b + c) / 2
    return s * (s - a) * (s - b) * (s - c)

if __name__ == '__main__':
    sides = {'a': 3, 'b': 4, 'c': 5}
    perimeter = calculate_triangle_perimeter(sides['a'], sides['b'], sides['c'])
    print(perimeter)