def is_non_degenerate_triangle(sides: tuple) -> bool:
    a, b, c = sorted(sides)
    return a + b > c

if __name__ == '__main__':
    sample_sides = (3.0, 4.0, 5.0)
    result = is_non_degenerate_triangle(sample_sides)
    print(result)