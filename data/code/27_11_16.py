def is_valid_triangle(sides):
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    sets = [(3, 4, 5), (1, 2, 3), (5, 5, 5), (10, 2, 5), (7, 8, 9), (0, 1, 1)]
    results = [is_valid_triangle(s) for s in sets]
    print(results)