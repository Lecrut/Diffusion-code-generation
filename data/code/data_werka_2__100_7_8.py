def evaluate_complex_condition(a: int, b: int, c: int, d: int) -> bool:
    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return False
    
    sum_ab = a + b
    product_cd = c * d
    
    if sum_ab > 100 and product_cd < 50:
        return True
    
    if sum_ab < 50 and product_cd > 200:
        return True
    
    if (a % 2 == 0 and b % 2 == 0) or (c % 2 != 0 and d % 2 != 0):
        if sum_ab == product_cd:
            return True
            
    return False

if __name__ == '__main__':
    result = evaluate_complex_condition(10, 20, 5, 10)
    print(result)