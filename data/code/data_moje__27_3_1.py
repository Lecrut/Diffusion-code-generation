def is_valid_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c

if __name__ == '__main__':
    sample_sides = (3, 4, 5)
    result = is_valid_triangle(sample_sides)
    print(result)