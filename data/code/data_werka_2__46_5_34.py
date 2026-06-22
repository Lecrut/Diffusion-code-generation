def calculate_triangle_perimeter(a, b, c):
    sides = {'a': a, 'b': b, 'c': c}
    return sum(sides.values())

if __name__ == '__main__':
    sample_values = {'a': 7.0, 'b': 9.2, 'c': 11.3}
    perimeter = calculate_triangle_perimeter(**sample_values)
    print(perimeter)