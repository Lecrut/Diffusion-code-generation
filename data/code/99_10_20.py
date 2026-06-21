def evaluate_complex_boolean(a, b, c, d):
    if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool) or not isinstance(d, bool):
        raise ValueError("All inputs must be boolean values.")
    
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
    expr11 = not a or not b and c
    expr12 = (a or b) and not c
    
    results = {
        "a and b or c": expr1,
        "(a and b) or c": expr2,
        "a and (b or c)": expr3,
        "not a and b or c": expr4,
        "not (a and b) or c": expr5,
        "a or b and c": expr6,
        "(a or b) and c": expr7,
        "not a or b and c": expr8,
        "not (a or b) and c": expr9,
        "a and not b or c": expr10,
        "not a or not b and c": expr11,
        "(a or b) and not c": expr12
    }
    return results

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    val_d = False
    
    computed_results = evaluate_complex_boolean(val_a, val_b, val_c, val_d)
    print(computed_results)