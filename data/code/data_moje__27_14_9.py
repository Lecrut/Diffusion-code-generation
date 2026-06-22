def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

def validate_sides(sides: list) -> bool:
    if len(sides) != 3:
        return False
    for side in sides:
        if not isinstance(side, (int, float)):
            return False
        if side <= 0:
            return False
    a, b, c = sides
    return is_valid_triangle(a, b, c)

if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    result = validate_sides(sample_sides)
    print(result)