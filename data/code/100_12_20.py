def parse_logical_statement(statement: str, **variables: bool) -> bool:
    tokens = statement.split()
    if not tokens:
        raise ValueError("Empty statement")
    
    result = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == 'AND':
            if result is None:
                raise ValueError("AND cannot be the first token")
            if i + 1 >= len(tokens):
                raise ValueError("AND must be followed by an operand")
            next_token = tokens[i + 1]
            if next_token in variables:
                val = variables[next_token]
            elif next_token == 'TRUE':
                val = True
            elif next_token == 'FALSE':
                val = False
            else:
                raise ValueError(f"Unknown variable: {next_token}")
            result = result and val
            i += 2
        elif token == 'OR':
            if result is None:
                raise ValueError("OR cannot be the first token")
            if i + 1 >= len(tokens):
                raise ValueError("OR must be followed by an operand")
            next_token = tokens[i + 1]
            if next_token in variables:
                val = variables[next_token]
            elif next_token == 'TRUE':
                val = True
            elif next_token == 'FALSE':
                val = False
            else:
                raise ValueError(f"Unknown variable: {next_token}")
            result = result or val
            i += 2
        elif token == 'NOT':
            if i + 1 >= len(tokens):
                raise ValueError("NOT must be followed by an operand")
            next_token = tokens[i + 1]
            if next_token in variables:
                val = variables[next_token]
            elif next_token == 'TRUE':
                val = True
            elif next_token == 'FALSE':
                val = False
            else:
                raise ValueError(f"Unknown variable: {next_token}")
            if result is None:
                result = not val
            else:
                result = result and (not val)
            i += 2
        elif token in variables:
            val = variables[token]
            if result is None:
                result = val
            else:
                result = result and val
            i += 1
        elif token == 'TRUE':
            val = True
            if result is None:
                result = val
            else:
                result = result and val
            i += 1
        elif token == 'FALSE':
            val = False
            if result is None:
                result = val
            else:
                result = result and val
            i += 1
        else:
            raise ValueError(f"Unknown token: {token}")
    
    if result is None:
        raise ValueError("No operands found")
    return result

if __name__ == '__main__':
    print(parse_logical_statement('A AND B', A=True, B=False))
    print(parse_logical_statement('A OR B', A=False, B=True))
    print(parse_logical_statement('A AND B OR C', A=True, B=True, C=False))
    print(parse_logical_statement('NOT A', A=True))
    print(parse_logical_statement('TRUE AND B', B=True))
    print(parse_logical_statement('A OR FALSE', A=False))