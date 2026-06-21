def is_valid_triangle(sides):
    a, b, c = sides
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    sample_sides = [(3, 4, 5), (1, 2, 3), (7, 10, 5), (0, 0, 0)]
    for sides in sample_sides:
        result = is_valid_triangle(sides)
        print(result)