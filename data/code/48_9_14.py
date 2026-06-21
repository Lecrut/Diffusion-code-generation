def is_valid_triangle(sides):
    if not isinstance(sides, list) or len(sides) != 3:
        return False
    if any(not isinstance(x, (int, float)) for x in sides):
        return False
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return validate_triangle_inequalities(a, b, c)

def validate_triangle_inequalities(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    sample_values = [
        [3, 4, 5],
        [1, 2, 3],
        [0, 4, 5],
        [-1, 4, 5],
        [5, 5, 5],
        [2, 2, 3],
        [7, 10, 5],
        [6, 6, 6],
        [8, 15, 17],
        [1, 1, 2],
        [0, 5, 5],
        [-3, 4, 5]
    ]
    for sides in sample_values:
        print(is_valid_triangle(sides))