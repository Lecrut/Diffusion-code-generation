def calculate_triangle_perimeter(a, b, c):
    sides = {'side1': a, 'side2': b, 'side3': c}
    perimeter = sum(sides.values())
    return perimeter

if __name__ == '__main__':
    side_lengths = {'a': 7, 'b': 8, 'c': 9}
    result = calculate_triangle_perimeter(side_lengths['a'], side_lengths['b'], side_lengths['c'])
    print(result)