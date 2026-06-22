import math

def verify_triangle_inequality(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    sum_ab = a + b
    sum_ac = a + c
    sum_bc = b + c
    
    cond_1 = sum_ab > c
    cond_2 = sum_ac > b
    cond_3 = sum_bc > a
    
    return cond_1 and cond_2 and cond_3

def check_with_tolerance(a: float, b: float, c: float, eps: float = 1e-9) -> bool:
    if a <= eps or b <= eps or c <= eps:
        return False
    
    if a + b < c + eps:
        return False
    if a + c < b + eps:
        return False
    if b + c < a + eps:
        return False
    
    return True

if __name__ == '__main__':
    values_a = 3.0
    values_b = 4.0
    values_c = 5.0
    
    result_standard = verify_triangle_inequality(values_a, values_b, values_c)
    print(result_standard)
    
    result_tolerant = check_with_tolerance(values_a, values_b, values_c)
    print(result_tolerant)
    
    values_degenerate_a = 1.0
    values_degenerate_b = 2.0
    values_degenerate_c = 3.0
    
    result_degenerate = verify_triangle_inequality(values_degenerate_a, values_degenerate_b, values_degenerate_c)
    print(result_degenerate)
    
    values_invalid_a = -1.0
    values_invalid_b = 2.0
    values_invalid_c = 2.0
    
    result_invalid = verify_triangle_inequality(values_invalid_a, values_invalid_b, values_invalid_c)
    print(result_invalid)