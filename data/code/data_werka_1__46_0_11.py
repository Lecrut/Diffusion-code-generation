def calculate_triangle_perimeter(a, b, c):
    sides = [a, b, c]
    if any(side <= 0 for side in sides) or not all(sides[i] + sides[j] > sides[k] for i, j, k in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]):
        return "Invalid triangle: The side lengths do not form a valid triangle."
    return sum(sides)

if __name__ == '__main__':
    sample_values = {'side1': 6, 'side2': 8, 'side3': 10}
    result = calculate_triangle_perimeter(sample_values['side1'], sample_values['side2'], sample_values['side3'])
    print(result)