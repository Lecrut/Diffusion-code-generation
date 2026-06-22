def evaluate_complex_boolean_expression(a, b, c, d):
    result1 = (a > b) and (c < d) or not (a == b)
    result2 = (a == b) or (c > d) and not (a < b)
    result3 = not ((a > b) and (c < d)) or (a == b)
    result4 = (a != b) and (c == d) or (a < b)
    result5 = ((a > b) or (c < d)) and (not (a == b))
    return {
        "expr1": result1,
        "expr2": result2,
        "expr3": result3,
        "expr4": result4,
        "expr5": result5
    }

if __name__ == '__main__':
    a_val = 10
    b_val = 5
    c_val = 3
    d_val = 8
    results = evaluate_complex_boolean_expression(a_val, b_val, c_val, d_val)
    print(results)