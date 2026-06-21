def check_valid_triangles(sides):
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a
    return [is_valid(a, b, c) for a, b, c in sides]

if __name__ == '__main__':
    sample_sides = [
        (3, 4, 5),
        (1, 2, 3),
        (10, 20, 25),
        (1, 1, 1),
        (5, 1, 2)
    ]
    print(check_valid_triangles(sample_sides))