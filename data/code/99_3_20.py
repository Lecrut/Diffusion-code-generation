def evaluate_complex_boolean(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    sample_expressions = [
        "True and False or True",
        "not (5 > 3) and (4 < 6)",
        "(10 == 10) or not (2 != 2)"
    ]
    for expr in sample_expressions:
        print(f"Evaluating: {expr} -> Result: {evaluate_complex_boolean(expr)}")