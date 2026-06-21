def is_non_degenerate_triangle(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return (a > 0) and (b > 0) and (c > 0) and (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    sample_sides = (3.0, 4.0, 5.0)
    result = is_non_degenerate_triangle(sample_sides)
    print(result)