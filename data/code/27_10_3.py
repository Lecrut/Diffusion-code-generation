def is_non_degenerate_triangle(coords):
    a, b, c = sorted(coords[:3])
    return a + b > c

if __name__ == '__main__':
    sample = (3.0, 4.0, 5.0)
    result = is_non_degenerate_triangle(sample)
    print(result)