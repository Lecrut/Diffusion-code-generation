def calculate_triangle_perimeter(a, b, c):
    sides = {'a': a, 'b': b, 'c': c}
    return sum(sides.values())

if __name__ == '__main__':
    sample_values = {'a': 3.5, 'b': 4.2, 'c': 5.1}
    perimeter = calculate_triangle_perimeter(**sample_values)
    print(perimeter)