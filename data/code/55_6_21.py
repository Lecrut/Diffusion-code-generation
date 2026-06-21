def calculate_triangle_perimeter(a, b, c):
    sides = {'a': a, 'b': b, 'c': c}
    for side_name, side_length in sides.items():
        if side_length <= 0:
            raise ValueError(f"Side {side_name} must be a positive number")
    return sum(sides.values())

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(6, 8, 10)
        print(perimeter)
    except ValueError as e:
        print(e)