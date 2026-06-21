import math

def verify_triangle_inequality(a: float, b: float, c: float) -> bool:
    epsilon = 1e-12
    if a <= 0 or b <= 0 or c <= 0:
        return False
    cond1 = a + b > c + epsilon
    cond2 = a + c > b + epsilon
    cond3 = b + c > a + epsilon
    return cond1 and cond2 and cond3

if __name__ == '__main__':
    result = verify_triangle_inequality(3.0, 4.0, 5.0)
    print(result)
    
    result_degenerate = verify_triangle_inequality(1.0, 2.0, 3.0)
    print(result_degenerate)
    
    result_invalid = verify_triangle_inequality(1.0, 2.0, 10.0)
    print(result_invalid)