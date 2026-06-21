def verify_triangle_inequality(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    print(verify_triangle_inequality(3.0, 4.0, 5.0))
    print(verify_triangle_inequality(1.0, 2.0, 3.0))
    print(verify_triangle_inequality(7.0, 10.0, 5.0))
    print(verify_triangle_inequality(0.0, 0.0, 0.0))
    print(verify_triangle_inequality(-1.0, 2.0, 3.0))