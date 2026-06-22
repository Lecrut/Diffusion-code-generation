def evaluate_boolean_logic(x, y, z):
    cond_1 = x > y
    cond_2 = z < x
    cond_3 = y == z
    term_1 = cond_1 and cond_2
    term_2 = not cond_3
    expression_1 = term_1 or term_2
    
    term_3 = x + y
    term_4 = z * 2
    cond_4 = term_3 > term_4
    cond_5 = x != z
    expression_2 = cond_4 and cond_5
    
    neg_1 = not (x > z)
    neg_2 = not (y < z)
    expression_3 = neg_1 or neg_2
    
    return expression_1, expression_2, expression_3

if __name__ == '__main__':
    val_x = 15
    val_y = 10
    val_z = 5
    exp1, exp2, exp3 = evaluate_boolean_logic(val_x, val_y, val_z)
    print(exp1)
    print(exp2)
    print(exp3)