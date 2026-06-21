def parse_logical_statement(statement: str, values: dict) -> bool:
    tokens = statement.split()
    if not tokens:
        raise ValueError("Empty statement")
    
    result = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == 'AND':
            if result is None:
                raise ValueError("AND at start of statement")
            if i + 1 >= len(tokens):
                raise ValueError("AND without right operand")
            right_val = values.get(tokens[i + 1])
            if right_val is None:
                raise ValueError(f"Unknown variable: {tokens[i + 1]}")
            result = result and right_val
            i += 2
        elif token == 'OR':
            if result is None:
                raise ValueError("OR at start of statement")
            if i + 1 >= len(tokens):
                raise ValueError("OR without right operand")
            right_val = values.get(tokens[i + 1])
            if right_val is None:
                raise ValueError(f"Unknown variable: {tokens[i + 1]}")
            result = result or right_val
            i += 2
        elif token == 'NOT':
            if i + 1 >= len(tokens):
                raise ValueError("NOT without operand")
            operand_val = values.get(tokens[i + 1])
            if operand_val is None:
                raise ValueError(f"Unknown variable: {tokens[i + 1]}")
            result = not operand_val
            i += 2
        else:
            if result is not None:
                raise ValueError("Unexpected token")
            val = values.get(token)
            if val is None:
                raise ValueError(f"Unknown variable: {token}")
            result = val
            i += 1
    
    if result is None:
        raise ValueError("No valid expression found")
    return result

if __name__ == '__main__':
    statement = 'A AND B'
    values = {'A': True, 'B': False}
    result = parse_logical_statement(statement, values)
    print(result)