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
            elif token in ('True', 'False'):
                parsed.append(token)
                i += 1
            elif token == '(':
                parsed.append(token)
                i += 1
            elif token == ')':
                parsed.append(token)
                i += 1
            else:
                parsed.append(token)
                i += 1
        return parsed
    parsed1 = parse_statement(stmt1)
    parsed2 = parse_statement(stmt2)
    if parsed1 is None or parsed2 is None:
        return False
    def evaluate(parsed):
        stack = []
        for token in parsed:
            if token == 'True':
                stack.append(True)
            elif token == 'False':
                stack.append(False)
            elif token == '(':
                stack.append('(')
            elif token == ')':
                stack.append(')')
            elif token == 'and':
                op = stack.pop()
                rhs = stack.pop()
                stack.append(op and rhs)
            elif token == 'or':
                op = stack.pop()
                rhs = stack.pop()
                stack.append(op or rhs)
            else:
                stack.append(token)
        return stack[0] if stack else None
    try:
        result1 = evaluate(parsed1)
        result2 = evaluate(parsed2)
        return result1 == result2
    except Exception:
        return False
if __name__ == '__main__':
    stmt_a = "if True and False: pass"
    stmt_b = "if True and False: pass"
    print(f"A: {stmt_a}, B: {stmt_b} -> {check_equivalence(stmt_a, stmt_b)}")
    stmt_c = "if True: pass"
    stmt_d = "if True: pass"
    print(f"C: {stmt_c}, D: {stmt_d} -> {check_equivalence(stmt_c, stmt_d)}")
    stmt_e = "if True: pass"
    stmt_f = "if False: pass"
    print(f"E: {stmt_e}, F: {stmt_f} -> {check_equivalence(stmt_e, stmt_f)}")
    stmt_g = "if True and False: pass"
    stmt_h = "if False and True: pass"
    print(f"G: {stmt_g}, H: {stmt_h} -> {check_equivalence(stmt_g, stmt_h)}")
    stmt_i = "if True: if False: pass"
    stmt_j = "if True: pass"
    print(f"I: {stmt_i}, J: {stmt_j} -> {check_equivalence(stmt_i, stmt_j)}")
    stmt_k = "if (True and False): pass"
    stmt_l = "if True and False: pass"
    print(f"K: {stmt_k}, L: {stmt_l} -> {check_equivalence(stmt_k, stmt_l)}")