def evaluate_logical_statement(statement: str, values: dict) -> bool:
    tokens = statement.split()
    if not tokens:
        raise ValueError("Empty statement")
    
    result = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in ('AND', 'OR'):
            if result is None:
                raise ValueError("Operator at start of expression")
            if i + 1 >= len(tokens):
                raise ValueError("Operator at end of expression")
            next_token = tokens[i + 1]
            if next_token in ('AND', 'OR'):
                raise ValueError("Consecutive operators")
            
            if next_token in values:
                operand = values[next_token]
            else:
                if next_token == 'True':
                    operand = True
                elif next_token == 'False':
                    operand = False
                else:
                    raise ValueError(f"Unknown variable: {next_token}")
            
            if token == 'AND':
                if result is None:
                    result = operand
                else:
                    result = result and operand
            elif token == 'OR':
                if result is None:
                    result = operand
                else:
                    result = result or operand
            
            i += 2
        else:
            if token in values:
                operand = values[token]
            else:
                if token == 'True':
                    operand = True
                elif token == 'False':
                    operand = False
                else:
                    raise ValueError(f"Unknown variable: {token}")
            
            if result is None:
                result = operand
            else:
                raise ValueError("Multiple operands without operator")
            i += 1
    
    if result is None:
        raise ValueError("No operands found")
    
    return result

if __name__ == '__main__':
    statement = 'A AND B'
    values = {'A': True, 'B': False}
    result = evaluate_logical_statement(statement, values)
    print(result)