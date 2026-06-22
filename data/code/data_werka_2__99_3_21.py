def evaluate_complex_expression(a, b, c, d):
    result1 = (a > b) and (c < d) or not (a == b)
    result2 = (a + b > c) and (d < a) or (b == c)
    result3 = not (a > b) and (c == d) or (a < b)
    result4 = (a != b) or (c > d) and not (a == c)
    return {
        "expr1": result1,
        "expr2": result2,
        "expr3": result3,
        "expr4": result4
    }

if __name__ == '__main__':
    values = evaluate_complex_expression(5, 3, 2, 8)
    print(values)