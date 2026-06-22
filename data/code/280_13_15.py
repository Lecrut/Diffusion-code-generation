def calculate_area(radius):
    return 3.14159 * radius ** 2

if __name__ == '__main__':
    radii = [1, 2, 3, 4, 5]
    areas = [calculate_area(r) for r in radii]
    print(areas)