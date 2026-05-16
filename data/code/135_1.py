def check_equivalence(stmt1, stmt2):
    def parse_statement(stmt):
        tokens = stmt.split()
        if not tokens:
            return None
        parsed = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token in ('if', 'and', 'or', 'not'):
                parsed.append(token)
                i += 1
            elif token == '(':
                parsed.append(token)
                i += 1
            elif token == ')':
                parsed.append(token)
                i += 1
            elif token.isalnum():
                parsed.append(token)
                i += 1
            else:
                i += 1
        return parsed
    def evaluate_expression(parsed_expr):
        if not parsed_expr:
            return False
        if len(parsed_expr) == 1:
            if parsed_expr[0] == 'True':
                return True
            if parsed_expr[0] == 'False':
                return False
            return False
        if parsed_expr[0] == 'not':
            operand = parsed_expr[1]
            if len(parsed_expr) == 3:
                return not evaluate_expression(parsed_expr[2])
            else:
                return False
        if parsed_expr[0] == 'and':
            left = evaluate_expression(parsed_expr[1])
            right = evaluate_expression(parsed_expr[2])
            return left and right
        if parsed_expr[0] == 'or':
            left = evaluate_expression(parsed_expr[1])
            right = evaluate_expression(parsed_expr[2])
            return left or right
        if parsed_expr[0] == 'if':
            if len(parsed_expr) == 3 and parsed_expr[1] in ('True', 'False'):
                return parsed_expr[2] == 'True'
            return False
        if parsed_expr[0] in ('True', 'False'):
            return parsed_expr[1] == 'True'
        return False
    def get_boolean_value(stmt):
        parsed = parse_statement(stmt)
        if not parsed:
            return None
        if len(parsed) > 0 and parsed[0] == 'if':
            if len(parsed) > 1:
                condition_tokens = parsed[1:]
                return evaluate_expression(condition_tokens)
        return evaluate_expression(parsed)
    val1 = get_boolean_value(stmt1)
    val2 = get_boolean_value(stmt2)
    return val1 == val2
if __name__ == '__main__':
    stmt_a = "if True and False: print('A')"
    stmt_b = "if False and True: print('B')"
    stmt_c = "True and False"
    stmt_d = "False and True"
    stmt_e = "if True: pass"
    stmt_f = "True"
    stmt_g = "if False: pass"
    stmt_h = "False"
    print(f"A vs B: {check_equivalence(stmt_a, stmt_b)}")
    print(f"C vs D: {check_equivalence(stmt_c, stmt_d)}")
    print(f"E vs F: {check_equivalence(stmt_e, stmt_f)}")
    print(f"G vs H: {check_equivalence(stmt_g, stmt_h)}")
    stmt_i = "if True and True"
    stmt_j = "True"
    print(f"I vs J: {check_equivalence(stmt_i, stmt_j)}")
    stmt_k = "if False"
    stmt_l = "False"
    print(f"K vs L: {check_equivalence(stmt_k, stmt_l)}")