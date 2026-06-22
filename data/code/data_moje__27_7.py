def verify_triangle_inequality(a, b, c):
    return a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0

if __name__ == '__main__':
    print(verify_triangle_inequality(3.0, 4.0, 5.0))
    print(verify_triangle_inequality(1.0, 2.0, 3.0))
    print(verify_triangle_inequality(10.0, 10.0, 10.0))
    print(verify_triangle_inequality(0.0, 5.0, 5.0))
    print(verify_triangle_inequality(-1.0, 2.0, 3.0))