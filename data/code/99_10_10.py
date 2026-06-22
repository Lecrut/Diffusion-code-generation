def evaluate_expression():
    a = True
    b = False
    c = True
    
    expr1 = a and b or c
    expr2 = a and (b or c)
    expr3 = (a or b) and c
    expr4 = not a and b or c
    expr5 = not (a and b) or c
    
    results = {
        "a and b or c": expr1,
        "a and (b or c)": expr2,
        "(a or b) and c": expr3,
        "not a and b or c": expr4,
        "not (a and b) or c": expr5
    }
    
    return results

if __name__ == '__main__':
    print(evaluate_expression())