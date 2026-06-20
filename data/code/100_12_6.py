def evaluate_logical_statement(statement, variables):
    parts = statement.split()
    if len(parts) != 3 or parts[1] not in ['AND', 'OR']:
        raise ValueError("Invalid logical statement format")
    
    left_var, operator, right_var = parts
    
    if left_var not in variables or right_var not in variables:
        raise ValueError("Variable not found in provided values")
    
    left_value = variables[left_var]
    right_value = variables[right_var]
    
    if operator == 'AND':
        return left_value and right_value
    elif operator == 'OR':
        return left_value or right_value

if __name__ == '__main__':
    variables = {'A': True, 'B': False}
    statement1 = 'A AND B'
    result1 = evaluate_logical_statement(statement1, variables)
    print(f"Statement '{statement1}' with variables {variables}: Result: {result1}")
    
    variables = {'X': True, 'Y': True}
    statement2 = 'X OR Y'
    result2 = evaluate_logical_statement(statement2, variables)
    print(f"Statement '{statement2}' with variables {variables}: Result: {result2}")