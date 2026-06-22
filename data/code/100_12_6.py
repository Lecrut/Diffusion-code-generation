def evaluate_logical_statement(statement: str, variables: dict) -> bool:
    tokens = statement.split()
    result = None
    for token in tokens:
        if token == 'AND':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            next_val = variables.get(tokens[tokens.index(token) + 1])
            if next_val is None:
                raise ValueError(f"Variable {tokens[tokens.index(token) + 1]} not found")
            result = result and next_val
        elif token == 'OR':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            next_val = variables.get(tokens[tokens.index(token) + 1])
            if next_val is None:
                raise ValueError(f"Variable {tokens[tokens.index(token) + 1]} not found")
            result = result or next_val
        elif token == 'NOT':
            next_val = variables.get(tokens[tokens.index(token) + 1])
            if next_val is None:
                raise ValueError(f"Variable {tokens[tokens.index(token) + 1]} not found")
            result = not next_val
        else:
            val = variables.get(token)
            if val is None:
                raise ValueError(f"Variable {token} not found")
            if result is None:
                result = val
            else:
                raise ValueError("Unsupported logical statement structure")
    if result is None:
        raise ValueError("Empty logical statement")
    return result

if __name__ == '__main__':
    variables = {'A': True, 'B': False}
    statement = 'A AND B'
    result = evaluate_logical_statement(statement, variables)
    print(result)