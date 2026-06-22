def evaluate_logic_expression(X, Y, Z, W):
    operators = {"and": lambda a, b: a and b, "or": lambda a, b: a or b, "not": lambda a: not a}
    
    def parse_term(term_val, var_val):
        bool_val = bool(var_val)
        return term_val(bool_val)
    
    term_w = parse_term(operators["not"], W)
    term_z = parse_term(lambda b: b, Z)
    
    and_wz = operators["and"](term_z, term_w)
    
    term_y = parse_term(lambda b: b, Y)
    term_x = parse_term(lambda b: b, X)
    
    and_xy = operators["and"](term_x, term_y)
    
    result = operators["or"](and_xy, and_wz)
    return result

if __name__ == '__main__':
    x_in = True
    y_in = False
    z_in = True
    w_in = False
    computed_result = evaluate_logic_expression(x_in, y_in, z_in, w_in)
    print(computed_result)