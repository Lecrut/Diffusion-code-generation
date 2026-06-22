def calculate_triangle_perimeter(a: float, b: float, c: float) -> float:
    return sum([a, b, c])

if __name__ == '__main__':
    sample_sides = {'side_a': 3.5, 'side_b': 4.2, 'side_c': 5.1}
    perimeter = calculate_triangle_perimeter(sample_sides['side_a'], sample_sides['side_b'], sample_sides['side_c'])
    print(perimeter)