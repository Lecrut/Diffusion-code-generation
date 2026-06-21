def validate_triangle_sides(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError("All sides must be numeric")
    if any(x <= 0 for x in (a, b, c)):
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    result = validate_triangle_sides(3, 4, 5)
    print(result)