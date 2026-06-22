def is_non_degenerate_triangle(sides: tuple[float, float, float]) -> bool:
    a, b, c = sorted(sides)
    return a + b > c

if __name__ == '__main__':
    result = is_non_degenerate_triangle((3.0, 4.0, 5.0))
    print(result)