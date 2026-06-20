def parse_logical_statement(statement, variables):
    if not isinstance(statement, str) or not isinstance(variables, dict):
        raise ValueError("Invalid input types")
    
    statement = statement.upper().replace(' ', '')
    if 'AND' not in statement:
        raise ValueError("Unsupported logical operator")
    
    parts = statement.split('AND')
    if len(parts) != 2:
        raise ValueError("Invalid statement format")
    
    left, right = parts
    if left not in variables or right not in variables:
        raise ValueError("Undefined variable in statement")
    
    return all(variables[var] for var in (left, right))

if __name__ == '__main__':
    vars1 = {'A': True, 'B': True}
    print(f"Statement: A AND B, Result: {parse_logical_statement('A AND B', vars1)}")
    
    vars2 = {'A': False, 'B': True}
    print(f"Statement: A AND B, Result: {parse_logical_statement('A AND B', vars2)}")