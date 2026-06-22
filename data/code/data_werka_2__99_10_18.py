TRUE_VAL = True
FALSE_VAL = False

def evaluate_logic(a, b, c):
    group1 = a and b
    group2 = b or c
    group3 = not a
    group4 = not b
    group5 = not c
    
    res1 = group1 or c
    res2 = a and group2
    res3 = group3 and b
    res4 = a or group4
    res5 = not (a and b)
    res6 = (a or b) and c
    res7 = a and (b or c)
    res8 = not a or (b and c)
    res9 = (a and not b) or c
    res10 = not (a or b) and c
    
    return {
        "a and b or c": res1,
        "a and (b or c)": res2,
        "not a and b": res3,
        "a or not b": res4,
        "not (a and b)": res5,
        "(a or b) and c": res6,
        "a and b or c (alt)": res7,
        "not a or b and c": res8,
        "a and not b or c": res9,
        "not (a or b) and c": res10
    }

if __name__ == '__main__':
    val_a = TRUE_VAL
    val_b = FALSE_VAL
    val_c = TRUE_VAL
    
    outcomes = evaluate_logic(val_a, val_b, val_c)
    
    for key, value in outcomes.items():
        print(f"{key}: {value}")