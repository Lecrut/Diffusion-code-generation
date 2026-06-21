def evaluate_expression():
    a = True
    b = False
    c = True
    d = False

    expr1 = a and b or c
    expr2 = (a and b) or c
    expr3 = a and (b or c)
    expr4 = not a and b or c
    expr5 = not (a and b) or c
    expr6 = a or b and c
    expr7 = (a or b) and c
    expr8 = not a or b and c
    expr9 = not (a or b) and c
    expr10 = a and not b or c

    results = [
        ("a and b or c", expr1),
        ("(a and b) or c", expr2),
        ("a and (b or c)", expr3),
        ("not a and b or c", expr4),
        ("not (a and b) or c", expr5),
        ("a or b and c", expr6),
        ("(a or b) and c", expr7),
        ("not a or b and c", expr8),
        ("not (a or b) and c", expr9),
        ("a and not b or c", expr10),
    ]

    return results

if __name__ == '__main__':
    results = evaluate_expression()
    for name, value in results:
        print(f"{name} = {value}")