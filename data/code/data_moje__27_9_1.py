def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    triplets = [
        (3, 4, 5),
        (1, 2, 3),
        (7, 10, 5),
        (2, 2, 8),
        (5, 5, 5),
        (0, 1, 2)
    ]
    results = [is_valid_triangle(x, y, z) for x, y, z in triplets]
    for result in results:
        print(result)