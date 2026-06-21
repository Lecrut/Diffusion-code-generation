def is_valid_triangle(sides):
    a, b, c = sides
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    sample_sides = (3, 4, 5)
    print(is_valid_triangle(sample_sides))