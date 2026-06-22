def evaluate_complex_condition(a: int, b: int, c: int, d: int) -> bool:
    if a <= 0 or b <= 0:
        return False
    if c < 0 or d < 0:
        return False
    sum_ab = a + b
    product_cd = c * d
    if sum_ab > 100:
        return product_cd > 50
    if sum_ab > 50:
        return product_cd > 25
    return product_cd > 10

if __name__ == '__main__':
    result = evaluate_complex_condition(10, 20, 5, 6)
    print(result)