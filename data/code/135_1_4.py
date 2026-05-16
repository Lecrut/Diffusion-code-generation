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
            else:
                if parsed and parsed[-1] == 'if':
                    condition = tokens[i]
                    parsed.append(condition)
                    i += 1
                else:
                    parsed.append(token)
                    i += 1
        return parsed
    def evaluate_expression(parsed_stmt):
        if not parsed_stmt:
            return None
        stack = []
        for token in parsed_stmt:
            if token == 'True':
                stack.append(True)
            elif token == 'False':
                stack.append(False)
            elif token == 'not':
                if len(stack) < 1: return None
                op = stack.pop()
                stack.append(not op)
            elif token == 'and':
                if len(stack) < 2: return None
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 and op2)
            elif token == 'or':
                if len(stack) < 2: return None
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 or op2)
            else:
                try:
                    stack.append(eval(token))
                except NameError:
                    return None
        if len(stack) == 1:
            return stack[0]
        return None
    try:
        parsed1 = parse_statement(stmt1)
        parsed2 = parse_statement(stmt2)
        if parsed1 is None or parsed2 is None:
            return False
        result1 = evaluate_expression(parsed1)
        result2 = evaluate_expression(parsed2)
        return result1 == result2
    except Exception:
        return False
if __name__ == '__main__':
    stmt_a = "if True and False: print('A')"
    stmt_b = "if False or True: print('B')"
    stmt_c = "if True: pass"
    stmt_d = "if True and True: pass"
    stmt_e = "if not True: pass"
    stmt_f = "if False: pass"
    print(f"A: {stmt_a}")
    print(f"B: {stmt_b}")
    print(f"C: {stmt_c}")
    print(f"D: {stmt_d}")
    print(f"E: {stmt_e}")
    print(f"F: {stmt_f}")
    print("-" * 20)
    print(f"A equivalent to B: {check_equivalence(stmt_a, stmt_b)}")
    print(f"C equivalent to D: {check_equivalence(stmt_c, stmt_d)}")
    print(f"E equivalent to F: {check_equivalence(stmt_e, stmt_f)}")
    print(f"A equivalent to A: {check_equivalence(stmt_a, stmt_a)}")
    print(f"B equivalent to C: {check_equivalence(stmt_b, stmt_c)}")
    print(f"D equivalent to A: {check_equivalence(stmt_d, stmt_a)}")