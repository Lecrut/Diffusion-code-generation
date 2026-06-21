def verify_triangle_inequality(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

if __name__ == '__main__':
    print(verify_triangle_inequality(3.0, 4.0, 5.0))
    print(verify_triangle_inequality(1.0, 2.0, 3.0))
    print(verify_triangle_inequality(0.5, 0.5, 0.5))
    print(verify_triangle_inequality(-1.0, 2.0, 3.0))