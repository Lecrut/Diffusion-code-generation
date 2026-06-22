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
    test_a = 3.0
    test_b = 4.0
    test_c = 5.0
    result = is_valid_triangle(test_a, test_b, test_c)
    print(result)
    test_x = 1.0
    test_y = 2.0
    test_z = 10.0
    result_2 = is_valid_triangle(test_x, test_y, test_z)
    print(result_2)
    test_p = 5.5
    test_q = 5.5
    test_r = 5.5
    result_3 = is_valid_triangle(test_p, test_q, test_r)
    print(result_3)
    test_m = -1.0
    test_n = 4.0
    test_o = 5.0
    result_4 = is_valid_triangle(test_m, test_n, test_o)
    print(result_4)