def is_valid_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c and a > 0 and b > 0 and c > 0

if __name__ == '__main__':
    sample_sides = (3, 4, 5)
    print(is_valid_triangle(sample_sides))