def calculate_triangle_perimeter(a, b, c):
    sides = {'a': a, 'b': b, 'c': c}
    invalid_sides = {side: length for side, length in sides.items() if length <= 0}
    if invalid_sides:
        raise ValueError(f"Invalid side lengths: {invalid_sides}")
    return sum(sides.values())

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(2, 3, 4)
        print(perimeter)
    except ValueError as e:
        print(e)