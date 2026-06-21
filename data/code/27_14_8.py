def validate_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    sides = [(3, 4, 5), (1, 2, 3), (10, 10, 10), (1, 1, 3), (-1, 2, 3)]
    results = [validate_triangle(a, b, c) for a, b, c in sides]
    print(results)