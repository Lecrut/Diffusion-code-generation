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
    expr10 = a and b and c or d

    results = {
        "expr1": expr1,
        "expr2": expr2,
        "expr3": expr3,
        "expr4": expr4,
        "expr5": expr5,
        "expr6": expr6,
        "expr7": expr7,
        "expr8": expr8,
        "expr9": expr9,
        "expr10": expr10
    }
    return results

if __name__ == '__main__':
    print(evaluate_expression())