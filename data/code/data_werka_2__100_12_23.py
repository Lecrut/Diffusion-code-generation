def evaluate_logical_statement(statement, variables):
    tokens = statement.split()
    result = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == 'AND':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            if i + 1 >= len(tokens):
                raise ValueError("Missing operand after AND")
            right = variables.get(tokens[i + 1])
            if right is None:
                raise ValueError(f"Variable {tokens[i + 1]} not found")
            result = result and right
            i += 2
        elif token == 'OR':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            if i + 1 >= len(tokens):
                raise ValueError("Missing operand after OR")
            right = variables.get(tokens[i + 1])
            if right is None:
                raise ValueError(f"Variable {tokens[i + 1]} not found")
            result = result or right
            i += 2
        elif token == 'NOT':
            if i + 1 >= len(tokens):
                raise ValueError("Missing operand after NOT")
            operand = variables.get(tokens[i + 1])
            if operand is None:
                raise ValueError(f"Variable {tokens[i + 1]} not found")
            result = not operand
            i += 2
        else:
            if result is None:
                val = variables.get(token)
                if val is None:
                    raise ValueError(f"Variable {token} not found")
                result = val
            else:
                raise ValueError("Invalid logical statement structure")
            i += 1
    return result

if __name__ == '__main__':
    variables = {'A': True, 'B': False}
    statement = 'A AND B'
    result = evaluate_logical_statement(statement, variables)
    print(result)