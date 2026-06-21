def is_valid_triangle_set(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0

def check_triangle_validity(triangle_sets):
    return [is_valid_triangle_set(s) for s in triangle_sets]

if __name__ == '__main__':
    sample_sets = [
        (3, 4, 5),
        (1, 2, 3),
        (7, 10, 5),
        (-1, 2, 3),
        (0, 0, 0),
        (10, 10, 10),
        (1, 1, 3)
    ]
    print(check_triangle_validity(sample_sets))