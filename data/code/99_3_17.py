def evaluate_complex_boolean():
    a = True
    b = False
    c = True
    x = 10
    y = 20
    z = 5

    expr1 = (a and b) or c
    expr2 = a and (b or c)
    expr3 = not (a and b)
    expr4 = x > y and y > z
    expr5 = x == y or y > z
    expr6 = not (x < y) and (z == 5)
    expr7 = (a or b) and (c or not b)
    expr8 = x > z and y < 30 or not c
    expr9 = (x == 10) and (y == 20) and (z == 5)
    expr10 = not (a and b and c)

    results = [expr1, expr2, expr3, expr4, expr5, expr6, expr7, expr8, expr9, expr10]
    return results

if __name__ == '__main__':
    print(evaluate_complex_boolean())