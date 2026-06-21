def calculate_triangle_perimeter(sides):
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = {
        'a': 7,
        'b': 24,
        'c': 25
    }
    sides_list = [triangle_sides['a'], triangle_sides['b'], triangle_sides['c']]
    perimeter = calculate_triangle_perimeter(sides_list)
    print(perimeter)