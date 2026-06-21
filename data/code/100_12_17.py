def parse_logical_statement(statement, variables):
    tokens = statement.split()
    result = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == 'AND':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            i += 1
            if i >= len(tokens):
                raise ValueError("Invalid logical statement structure")
            right = variables.get(tokens[i], False)
            result = result and right
        elif token == 'OR':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            i += 1
            if i >= len(tokens):
                raise ValueError("Invalid logical statement structure")
            right = variables.get(tokens[i], False)
            result = result or right
        elif token == 'NOT':
            i += 1
            if i >= len(tokens):
                raise ValueError("Invalid logical statement structure")
            operand = variables.get(tokens[i], False)
            result = not operand
        else:
            if result is None:
                result = variables.get(token, False)
            else:
                raise ValueError("Invalid logical statement structure")
        i += 1
    if result is None:
        raise ValueError("Empty logical statement")
    return result

if __name__ == '__main__':
    variables = {'A': True, 'B': False}
    statement = 'A AND B'
    result = parse_logical_statement(statement, variables)
    print(result)