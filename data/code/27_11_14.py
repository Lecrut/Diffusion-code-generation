def is_valid_triangle(sides):
    sides = sorted(sides)
    return len(sides) == 3 and sides[0] > 0 and sides[0] + sides[1] > sides[2]

def check_sides_array(sides_sets):
    return [is_valid_triangle(sides) for sides in sides_sets]

if __name__ == '__main__':
    sample_sets = [[3, 4, 5], [1, 2, 3], [7, 10, 2], [5, 5, 5], [1, 10, 12]]
    results = check_sides_array(sample_sets)
    print(results)