def is_valid_triangle(a, b, c):
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
    a, b, c = 3, 4, 5
    result = is_valid_triangle(a, b, c)
    print(result)
    
    a2, b2, c2 = 1, 2, 3
    result2 = is_valid_triangle(a2, b2, c2)
    print(result2)
    
    a3, b3, c3 = 0, 0, 0
    result3 = is_valid_triangle(a3, b3, c3)
    print(result3)