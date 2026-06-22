def evaluate_complex_expression(a, b, c, d):
    result1 = (a > b) and (c < d) or not (a == b)
    result2 = (a + b > c) and (d != a) or (b < c and d > a)
    result3 = not ((a > b) and (c == d)) or (a < b)
    result4 = (a == b) or (c > d) and (not (a < b))
    result5 = ((a > b) and (c < d)) or (a == b) and (not (c == d))
    return {
        "expr1": result1,
        "expr2": result2,
        "expr3": result3,
        "expr4": result4,
        "expr5": result5
    }

if __name__ == '__main__':
    values = evaluate_complex_expression(5, 3, 10, 2)
    print(values)