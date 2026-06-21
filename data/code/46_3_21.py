def calculate_triangle_perimeter(sides):
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = {
        'side1': 3,
        'side2': 4,
        'side3': 5
    }
    sides_list = [triangle_sides['side1'], triangle_sides['side2'], triangle_sides['side3']]
    perimeter = calculate_triangle_perimeter(sides_list)
    print(perimeter)