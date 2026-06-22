def get_perimeter(sides):
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = (6, 8, 10)
    perimeter = get_perimeter(triangle_sides)
    print(perimeter)