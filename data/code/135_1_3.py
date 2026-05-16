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
            else:
                parsed.append(token)
                i += 1
        return parsed
    def evaluate_logic(parsed_stmt):
        return parsed_stmt
    parsed1 = parse_statement(stmt1)
    parsed2 = parse_statement(stmt2)
    if parsed1 is None or parsed2 is None:
        return parsed1 == parsed2
    return parsed1 == parsed2
if __name__ == '__main__':
    stmt_a = "if x and y: print(1)"
    stmt_b = "if y and x: print(1)"
    stmt_c = "if x: print(1)"
    stmt_d = "if x and y: print(1)"
    stmt_e = "if x: if y: print(1)"
    stmt_f = "if y and x: print(1)"
    print(f"A vs D: {check_equivalence(stmt_a, stmt_d)}")
    print(f"A vs B: {check_equivalence(stmt_a, stmt_b)}")
    print(f"C vs D: {check_equivalence(stmt_c, stmt_d)}")
    print(f"E vs F: {check_equivalence(stmt_e, stmt_f)}")
    print(f"A vs E: {check_equivalence(stmt_a, stmt_e)}")
    print(f"C vs A: {check_equivalence(stmt_c, stmt_a)}")