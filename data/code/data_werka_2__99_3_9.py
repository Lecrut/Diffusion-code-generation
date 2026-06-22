def evaluate_complex_boolean(a, b, c, d, e):
    result1 = (a > b) and (c < d) or (not e)
    result2 = (a == b) or (c > d) and (not e)
    result3 = not ((a < b) and (c == d)) or (e > a)
    result4 = (a >= b) and (not (c <= d)) or (e == a)
    result5 = (a != b) or (c >= d) and (not (e < a))
    return result1, result2, result3, result4, result5

if __name__ == '__main__':
    a_val = 10
    b_val = 5
    c_val = 3
    d_val = 8
    e_val = False

    res1, res2, res3, res4, res5 = evaluate_complex_boolean(a_val, b_val, c_val, d_val, e_val)
    print(res1)
    print(res2)
    print(res3)
    print(res4)
    print(res5)