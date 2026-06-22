def calculate_perimeter(sides):
    side_map = {0: 'first', 1: 'second', 2: 'third'}
    for index, side in enumerate(sides):
        if side <= 0:
            raise ValueError(f"The {side_map[index]} side must be a positive number.")
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = [5, 12, 13]
    perimeter_value = calculate_perimeter(triangle_sides)
    print(perimeter_value)