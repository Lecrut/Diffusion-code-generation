def is_non_degenerate_triangle(coords: tuple[float, float, float]) -> bool:
    a, b, c = coords
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    result = is_non_degenerate_triangle((3.0, 4.0, 5.0))
    print(result)