VALID_TRIANGLE_CONDITIONS = (3,)
SAMPLE_SIDE_SETS = [
    [3, 4, 5],
    [1, 2, 3],
    [10, 15, 20],
    [1, 1, 1],
    [0, 5, 5],
    [7, 8, 9],
    [2, 2, 4],
    [10, 24, 26],
    [5, 5, 9],
    [100, 1, 1]
]

def is_valid_triangle_set(sides):
    if len(sides) != 3:
        return False
    sorted_sides = sorted(sides)
    smallest = sorted_sides[0]
    middle = sorted_sides[1]
    largest = sorted_sides[2]
    if smallest <= 0:
        return False
    if middle <= 0:
        return False
    if largest <= 0:
        return False
    if smallest + middle > largest:
        return True
    return False

def validate_triangle_sets(side_length_sets):
    results = []
    for sides in side_length_sets:
        valid = is_valid_triangle_set(sides)
        results.append(valid)
    return results

if __name__ == '__main__':
    output = validate_triangle_sets(SAMPLE_SIDE_SETS)
    print(output)