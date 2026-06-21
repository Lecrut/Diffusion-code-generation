def evaluate_complex_boolean_expression(a, b, c, d):
    result1 = (a > b) and (c < d) or not (a == b)
    result2 = (a == b) or (c > d) and not (a < b)
    result3 = not ((a > b) and (c == d)) or (a < b)
    result4 = (a != b) and ((c > d) or (a == c))
    result5 = (a + b > c) and (d - a < b) or (c * 2 == d)
    return {
        "expr1": result1,
        "expr2": result2,
        "expr3": result3,
        "expr4": result4,
        "expr5": result5
    }

if __name__ == '__main__':
    sample_values = {
        "a": 10,
        "b": 5,
        "c": 3,
        "d": 8
    }
    results = evaluate_complex_boolean_expression(
        sample_values["a"],
        sample_values["b"],
        sample_values["c"],
        sample_values["d"]
    )
    print(results)