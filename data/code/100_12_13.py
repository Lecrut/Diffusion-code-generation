def evaluate_logical_statement(statement: str, variables: dict) -> bool:
    tokens = statement.split()
    if not tokens:
        raise ValueError("Empty statement")
    
    result = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == 'AND':
            if result is None:
                raise ValueError("AND cannot be the first operator")
            if i + 1 >= len(tokens):
                raise ValueError("AND requires a right operand")
            right_val = _get_value(tokens[i + 1], variables)
            result = result and right_val
            i += 2
        elif token == 'OR':
            if result is None:
                raise ValueError("OR cannot be the first operator")
            if i + 1 >= len(tokens):
                raise ValueError("OR requires a right operand")
            right_val = _get_value(tokens[i + 1], variables)
            result = result or right_val
            i += 2
        elif token == 'NOT':
            if i + 1 >= len(tokens):
                raise ValueError("NOT requires an operand")
            operand_val = _get_value(tokens[i + 1], variables)
            result = not operand_val
            i += 2
        else:
            val = _get_value(token, variables)
            if result is None:
                result = val
            else:
                raise ValueError("Unexpected operand without operator")
            i += 1
            
    if result is None:
        raise ValueError("No result computed")
    return result

def _get_value(token: str, variables: dict) -> bool:
    if token.upper() in ('TRUE', '1'):
        return True
    if token.upper() in ('FALSE', '0'):
        return False
    if token in variables:
        return bool(variables[token])
    raise ValueError(f"Unknown variable or value: {token}")

if __name__ == '__main__':
    variables = {'A': True, 'B': False}
    statement = 'A AND B'
    result = evaluate_logical_statement(statement, variables)
    print(result)