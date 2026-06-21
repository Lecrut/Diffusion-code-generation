def _parse_statement(statement):
    parts = statement.split(' if ')
    if len(parts) == 2:
        antecedent, consequent = (parts[0].strip(), parts[1].strip())
        return (antecedent, consequent)
    else:
        return (statement, 'Malformed')

def _is_mutually_exclusive(condition1, condition2):
    if 'not' in condition1 and condition1.replace(' not', '') in condition2:
        return True
    return False

def analyze_logic(statements):
    parsed_statements = [_parse_statement(stmt) for stmt in statements]
    contradictions = []
    n = len(parsed_statements)
    for i in range(n):
        for j in range(i + 1, n):
            antecedent_i, consequent_i = parsed_statements[i]
            antecedent_j, consequent_j = parsed_statements[j]
            if _is_mutually_exclusive(antecedent_i, antecedent_j) and _is_mutually_exclusive(consequent_i, consequent_j):
                contradictions.append((i, j))
    return contradictions
if __name__ == '__main__':
    statements = ['The sky is blue if it is day', 'It is night if the sun is not shining', 'If it is day and the sun is shining, then it is not night']
    result = analyze_logic(statements)
    print(result)