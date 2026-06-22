def evaluate_complex_expression(a, b, c, d):
    result1 = (a > b) and (c < d) or not (a == b)
    result2 = (a + b > c) and (d < 10) or (a == 0)
    result3 = not ((a > b) and (c == d)) or (b < a)
    result4 = (a < b) or (c > d) and (a != b)
    result5 = ((a + b) > (c * d)) and (not (a == 0))
    results = [result1, result2, result3, result4, result5]
    return results

if __name__ == '__main__':
    a_val = 5
    b_val = 3
    c_val = 4
    d_val = 6
    output = evaluate_complex_expression(a_val, b_val, c_val, d_val)
    print(output)