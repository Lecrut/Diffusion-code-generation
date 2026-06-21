def is_valid_triangle(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0

if __name__ == '__main__':
    sample_tuples = ((3, 4, 5), (1, 2, 3), (7, 10, 5), (1, 1, 3))
    results = []
    for t in sample_tuples:
        results.append(is_valid_triangle(t))
    print(results)