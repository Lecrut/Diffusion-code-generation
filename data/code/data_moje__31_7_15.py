def compute_square_areas(sides):
    return [side * side for side in sides]

if __name__ == '__main__':
    lengths = [2, 5, 10]
    areas = compute_square_areas(lengths)
    print(areas)