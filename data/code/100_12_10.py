def evaluate_logical_statement(statement, values):
    tokens = statement.split()
    if not tokens:
        raise ValueError("Empty statement")
    
    result = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in ('AND', 'OR'):
            if result is None:
                raise ValueError("Logical operator at start of expression")
            if i + 1 >= len(tokens):
                raise ValueError("Operator at end of expression")
            next_token = tokens[i + 1]
            if next_token in ('AND', 'OR'):
                raise ValueError("Consecutive operators")
            val = values.get(next_token, False)
            if token == 'AND':
                result = result and val
            else:
                result = result or val
            i += 2
        else:
            val = values.get(token, False)
            if result is None:
                result = val
            else:
                raise ValueError("Missing operator between operands")
            i += 1
    
    if result is None:
        raise ValueError("No operands found")
    
    return result

if __name__ == '__main__':
    statement = 'A AND B'
    values = {'A': True, 'B': False}
    print(evaluate_logical_statement(statement, values))