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
    sample_a = 3.0
    sample_b = 4.0
    sample_c = 5.0
    result = verify_triangle_inequality(sample_a, sample_b, sample_c)
    print(result)