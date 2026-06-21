def evaluate_triangle(a: float, b: float, c: float) -> dict:
    if a <= 0 or b <= 0 or c <= 0:
        return {"valid": False, "reason": "Sides must be positive"}
    if a + b <= c or a + c <= b or b + c <= a:
        return {"valid": False, "reason": "Triangle inequality violated"}
    if a == b == c:
        triangle_type = "equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"
    return {"valid": True, "type": triangle_type}

if __name__ == '__main__':
    configurations = [
        (3, 4, 5),
        (7, 7, 7),
        (5, 5, 8),
        (1, 2, 3),
        (-1, 2, 3),
        (0, 5, 5)
    ]
    for sides in configurations:
        result = evaluate_triangle(*sides)
        print(f"Sides {sides}: {result}")