def is_valid_triangle(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    samples = [
        (3, 4, 5),
        (1, 2, 3),
        (0, 4, 5),
        (5, 5, 10),
        (7, 10, 5)
    ]
    for s in samples:
        result = is_valid_triangle(s)
        print(result)