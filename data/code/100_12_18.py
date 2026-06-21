def evaluate_logical_statement(statement, variables):
    tokens = statement.split()
    result = None
    for token in tokens:
        if token == 'AND':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            if result is False:
                continue
        elif token == 'OR':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            if result is True:
                continue
        elif token == 'NOT':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            result = not result
            continue
        else:
            if token not in variables:
                raise ValueError(f"Variable '{token}' not provided")
            val = variables[token]
            if result is None:
                result = val
            elif token == 'AND':
                result = result and val
            elif token == 'OR':
                result = result or val
            else:
                raise ValueError(f"Unsupported operator '{token}'")
    if result is None:
        raise ValueError("Empty logical statement")
    return result

if __name__ == '__main__':
    statement = "A AND B"
    variables = {"A": True, "B": False}
    result = evaluate_logical_statement(statement, variables)
    print(result)