def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    samples = [(3, 4, 5), (1, 2, 3), (10, 1, 1), (5, 5, 5)]
    for sides in samples:
        result = is_valid_triangle(*sides)
        print(f"{sides}: {result}")