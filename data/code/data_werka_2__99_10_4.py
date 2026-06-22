def evaluate_expression():
    a = True
    b = False
    c = True

    result1 = a and b or c
    result2 = (a and b) or c
    result3 = a and (b or c)
    result4 = not a and b or c
    result5 = not (a and b) or c
    result6 = a or b and c
    result7 = (a or b) and c
    result8 = not a or b and c
    result9 = not (a or b) and c
    result10 = a and not b or c

    return {
        "a and b or c": result1,
        "(a and b) or c": result2,
        "a and (b or c)": result3,
        "not a and b or c": result4,
        "not (a and b) or c": result5,
        "a or b and c": result6,
        "(a or b) and c": result7,
        "not a or b and c": result8,
        "not (a or b) and c": result9,
        "a and not b or c": result10
    }

if __name__ == '__main__':
    results = evaluate_expression()
    for expr, val in results.items():
        print(f"{expr} = {val}")