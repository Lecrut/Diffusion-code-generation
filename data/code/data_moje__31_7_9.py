def calculate_square_areas(sides):
    return [side * side for side in sides]

if __name__ == '__main__':
    sample_sides = [2, 4, 5, 8]
    areas = calculate_square_areas(sample_sides)
    print(areas)