def calculate_triangle_perimeter(sides):
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = {
        'a': 5,
        'b': 12,
        'c': 13
    }
    sides_list = [triangle_sides[key] for key in sorted(triangle_sides.keys())]
    perimeter = calculate_triangle_perimeter(sides_list)
    print(perimeter)