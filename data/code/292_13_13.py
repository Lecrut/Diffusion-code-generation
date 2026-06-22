def calculate_polygon_perimeter(sides):
    perimeter = sum(sides)
    return perimeter

if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    print(calculate_polygon_perimeter(sample_sides))