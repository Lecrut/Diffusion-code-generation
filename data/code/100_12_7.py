def evaluate_logical_statement(statement, values):
    tokens = statement.split()
    result = None
    for token in tokens:
        if token == 'AND':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            if result is False:
                continue
            if values.get(tokens[tokens.index(token) + 1]) is None:
                raise ValueError("Missing value for operand")
            result = result and values.get(tokens[tokens.index(token) + 1])
        elif token == 'OR':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            if result is True:
                continue
            if values.get(tokens[tokens.index(token) + 1]) is None:
                raise ValueError("Missing value for operand")
            result = result or values.get(tokens[tokens.index(token) + 1])
        elif token == 'NOT':
            if values.get(tokens[tokens.index(token) + 1]) is None:
                raise ValueError("Missing value for operand")
            result = not values.get(tokens[tokens.index(token) + 1])
        else:
            if values.get(token) is None:
                raise ValueError(f"Missing value for variable {token}")
            if result is None:
                result = values.get(token)
            else:
                raise ValueError("Invalid logical statement structure")
    return result

if __name__ == '__main__':
    statement = 'A AND B'
    values = {'A': True, 'B': False}
    result = evaluate_logical_statement(statement, values)
    print(result)