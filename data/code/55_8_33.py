def calculate_triangle_perimeter(a, b, c):
    sides = {'a': a, 'b': b, 'c': c}
    for side, length in sides.items():
        if length <= 0:
            raise ValueError(f"Side {side} must be a positive number.")
    return sum(sides.values())

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(9, 12, 15)
        print(perimeter)
    except ValueError as e:
        print(e)