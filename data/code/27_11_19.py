def check_triangle_sides(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and (b + c > a)

def validate_all_sides(sides_sets):
    return [check_triangle_sides(sides) for sides in sides_sets]
if __name__ == '__main__':
    sample_sides = [[3, 4, 5], [1, 2, 3], [0, 0, 0], [5, 5, 5], [10, 2, 1], [-1, 5, 5], [7, 8, 9]]
    results = validate_all_sides(sample_sides)
    print(results)