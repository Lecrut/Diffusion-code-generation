def evaluate_logical_statement(statement, variables):
    tokens = statement.split()
    result = None
    for token in tokens:
        if token == 'AND':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            if result is False:
                continue
            if variables.get('B') is None:
                raise ValueError("Missing variable B")
            result = result and variables['B']
        elif token == 'OR':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            if result is True:
                continue
            if variables.get('B') is None:
                raise ValueError("Missing variable B")
            result = result or variables['B']
        elif token == 'NOT':
            if result is None:
                raise ValueError("Invalid logical statement structure")
            if variables.get('B') is None:
                raise ValueError("Missing variable B")
            result = not variables['B']
        elif token in ('A', 'B'):
            if token == 'A':
                if variables.get('A') is None:
                    raise ValueError("Missing variable A")
                val = variables['A']
            else:
                if variables.get('B') is None:
                    raise ValueError("Missing variable B")
                val = variables['B']
            if result is None:
                result = val
            else:
                raise ValueError("Invalid logical statement structure")
        else:
            raise ValueError(f"Unknown token: {token}")
    if result is None:
        raise ValueError("Empty logical statement")
    return result

if __name__ == '__main__':
    print(evaluate_logical_statement('A AND B', {'A': True, 'B': False}))
    print(evaluate_logical_statement('A OR B', {'A': False, 'B': True}))
    print(evaluate_logical_statement('A', {'A': True}))
    print(evaluate_logical_statement('NOT B', {'A': True, 'B': False}))