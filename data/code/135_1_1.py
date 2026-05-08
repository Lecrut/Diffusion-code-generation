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
                if token == 'if':
                    i += 1
                    if i < len(tokens) and tokens[i] == 'then':
                        i += 1
                        condition_tokens = []
                        while i < len(tokens) and tokens[i] not in ('else', 'and', 'or', 'if'):
                            condition_tokens.append(tokens[i])
                            i += 1
                        condition = " ".join(condition_tokens)
                        parsed.append(('if', condition))
                    else:
                        parsed.append(('if', None))
                elif token == 'not':
                    if i + 1 < len(tokens):
                        parsed.append(('not', tokens[i+1]))
                        i += 1
                    else:
                        parsed.append(('not', None))
                elif token == 'and' or token == 'or':
                    parsed.append((token, None))
                else:
                    parsed.append((token, None))
            else:
                parsed.append((token, None))
            i += 1
        return parsed
    def evaluate_condition(condition):
        if condition is None:
            return None
        return condition
    parsed1 = parse_statement(stmt1)
    parsed2 = parse_statement(stmt2)
    if not parsed1 or not parsed2:
        return False
    if len(parsed1) != len(parsed2):
        return False
    for p1, p2 in zip(parsed1, parsed2):
        if p1[0] != p2[0]:
            return False
        if p1[0] == 'if':
            if p1[1] != p2[1]:
                return False
        elif p1[0] in ('and', 'or', 'not'):
            if p1[1] != p2[1]:
                return False
    return True
if __name__ == '__main__':
    stmt_a = "if condition1 then statement1"
    stmt_b = "if condition1 then statement1"
    stmt_c = "if condition1 then statement2"
    stmt_d = "if condition2 then statement1"
    stmt_e = "if condition1 then statement1 and statement2"
    stmt_f = "if condition1 then statement1 and statement2"
    stmt_g = "if condition1 then statement1"
    stmt_h = "if condition1 then statement1 and statement2"
    stmt_i = "if condition1 then statement1"
    stmt_j = "if condition1 then statement1"
    print(f"A vs B: {check_equivalence(stmt_a, stmt_b)}")
    print(f"A vs C: {check_equivalence(stmt_a, stmt_c)}")
    print(f"A vs D: {check_equivalence(stmt_a, stmt_d)}")
    print(f"E vs F: {check_equivalence(stmt_e, stmt_f)}")
    print(f"G vs I: {check_equivalence(stmt_g, stmt_i)}")
    print(f"A vs E: {check_equivalence(stmt_a, stmt_e)}")
    print(f"A vs H: {check_equivalence(stmt_a, stmt_h)}")
    print(f"A vs J: {check_equivalence(stmt_a, stmt_j)}")