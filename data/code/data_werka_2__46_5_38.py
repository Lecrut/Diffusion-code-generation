def calculate_triangle_perimeter(a, b, c):
    sides = {'a': a, 'b': b, 'c': c}
    perimeter = sum(sides.values())
    return perimeter

if __name__ == '__main__':
    sample_values = {'a': 5.0, 'b': 7.2, 'c': 9.3}
    try:
        perimeter = calculate_triangle_perimeter(**sample_values)
        print(perimeter)
    except ValueError as e:
        print(e)