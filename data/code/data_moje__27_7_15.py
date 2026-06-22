def verify_triangle_inequality(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

if __name__ == '__main__':
    sample_sides = [3.0, 4.0, 5.0]
    result = verify_triangle_inequality(*sample_sides)
    print(result)