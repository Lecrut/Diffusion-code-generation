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
                raise ValueError("AND at start of expression")
            if i + 1 >= len(tokens):
                raise ValueError("AND without right operand")
            right_val = variables.get(tokens[i + 1])
            if right_val is None:
                raise ValueError(f"Variable {tokens[i + 1]} not provided")
            result = result and right_val
            i += 2
        elif token == 'OR':
            if result is None:
                raise ValueError("OR at start of expression")
            if i + 1 >= len(tokens):
                raise ValueError("OR without right operand")
            right_val = variables.get(tokens[i + 1])
            if right_val is None:
                raise ValueError(f"Variable {tokens[i + 1]} not provided")
            result = result or right_val
            i += 2
        elif token == 'NOT':
            if i + 1 >= len(tokens):
                raise ValueError("NOT without operand")
            operand_name = tokens[i + 1]
            operand_val = variables.get(operand_name)
            if operand_val is None:
                raise ValueError(f"Variable {operand_name} not provided")
            result = not operand_val
            i += 2
        else:
            val = variables.get(token)
            if val is None:
                raise ValueError(f"Variable {token} not provided")
            if result is None:
                result = val
            else:
                raise ValueError("Unexpected variable without operator")
            i += 1
    
    if result is None:
        raise ValueError("No result computed")
    return result

if __name__ == '__main__':
    print(parse_logical_statement('A AND B', A=True, B=False))
    print(parse_logical_statement('A OR B', A=False, B=True))
    print(parse_logical_statement('NOT A', A=True))
    print(parse_logical_statement('A AND B OR C', A=True, B=False, C=True))