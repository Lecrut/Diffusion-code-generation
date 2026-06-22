TRUE_VAL = True
FALSE_VAL = False

def evaluate_logic():
    a = TRUE_VAL
    b = FALSE_VAL
    c = TRUE_VAL
    d = FALSE_VAL
    res1 = a and b or c
    res2 = (a and b) or c
    res3 = a and (b or c)
    res4 = not a and b or c
    res5 = not (a and b) or c
    res6 = a or b and c
    res7 = (a or b) and c
    res8 = not a or b and c
    res9 = not (a or b) and c
    res10 = a and not b or c
    res11 = (a or b) and (c or d)
    res12 = not (a or b) and (c and d)
    res13 = a or (b and c) or d
    res14 = (a and c) or (b and d)
    res15 = not a or not b
    return [
        ("a and b or c", res1),
        ("(a and b) or c", res2),
        ("a and (b or c)", res3),
        ("not a and b or c", res4),
        ("not (a and b) or c", res5),
        ("a or b and c", res6),
        ("(a or b) and c", res7),
        ("not a or b and c", res8),
        ("not (a or b) and c", res9),
        ("a and not b or c", res10),
        ("(a or b) and (c or d)", res11),
        ("not (a or b) and (c and d)", res12),
        ("a or (b and c) or d", res13),
        ("(a and c) or (b and d)", res14),
        ("not a or not b", res15),
    ]

if __name__ == '__main__':
    results = evaluate_logic()
    for expr, val in results:
        print(f"{expr} = {val}")