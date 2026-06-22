def verify_triangle_inequality(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    a_val = 3.0
    b_val = 4.0
    c_val = 5.0
    result = verify_triangle_inequality(a_val, b_val, c_val)
    print(result)