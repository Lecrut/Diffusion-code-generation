def evaluate_complex_expression(a, b, c, d):
    result1 = (a > b) and (c < d) or not (a == b)
    result2 = (a + b > c) and (d < 10) or (a == 0)
    result3 = not ((a > b) and (c == d)) or (b < a)
    result4 = (a != b) or (c > d) and (a < 100)
    return result1, result2, result3, result4

if __name__ == '__main__':
    a_val = 10
    b_val = 5
    c_val = 20
    d_val = 15
    res1, res2, res3, res4 = evaluate_complex_expression(a_val, b_val, c_val, d_val)
    print(res1)
    print(res2)
    print(res3)
    print(res4)