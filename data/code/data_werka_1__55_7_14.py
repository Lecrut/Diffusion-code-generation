def calculate_triangle_perimeter(a, b, c):
    sides = {'a': a, 'b': b, 'c': c}
    if not all(isinstance(x, (int, float)) and x > 0 for x in sides.values()):
        raise ValueError("All sides must be positive numbers")
    return sum(sides.values())

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(5, 12, 13)
        print(perimeter)
    except ValueError as e:
        print(e)