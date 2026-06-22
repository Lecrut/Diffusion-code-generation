def is_valid_triangle(sides):
    a, b, c = sides
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    samples = [(3, 4, 5), (1, 2, 3), (5, 5, 5)]
    for side_tuple in samples:
        print(is_valid_triangle(side_tuple))