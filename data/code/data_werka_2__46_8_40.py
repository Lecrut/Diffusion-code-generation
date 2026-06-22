def calculate_triangle_perimeter(side1, side2, side3):
    sides = [side1, side2, side3]
    if not all(isinstance(x, (int, float)) and x > 0 for x in sides):
        raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_sides = {
        'a': 7,
        'b': 8,
        'c': 9
    }
    perimeter = calculate_triangle_perimeter(sample_sides['a'], sample_sides['b'], sample_sides['c'])
    print(perimeter)