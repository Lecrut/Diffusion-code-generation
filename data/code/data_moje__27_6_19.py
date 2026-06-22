def get_triangle_status(a, b, c):
    def validate_positive(side, name):
        if side <= 0:
            raise ValueError(f"Side {name} must be positive")

    def validate_inequality(s1, s2, s3):
        if s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
            raise ValueError("Sides violate triangle inequality")

    validate_positive(a, 'a')
    validate_positive(b, 'b')
    validate_positive(c, 'c')
    validate_inequality(a, b, c)

    if a == b and b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"

if __name__ == '__main__':
    print(get_triangle_status(3, 4, 5))
    print(get_triangle_status(5, 5, 5))
    print(get_triangle_status(5, 5, 8))
    try:
        get_triangle_status(-1, 2, 3)
    except ValueError:
        print("invalid")
    try:
        get_triangle_status(1, 2, 3)
    except ValueError:
        print("invalid")