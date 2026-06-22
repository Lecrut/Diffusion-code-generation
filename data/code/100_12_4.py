def evaluate_logical_statement(statement: str, values: dict) -> bool:
    tokens = statement.split()
    if len(tokens) != 3:
        raise ValueError("Statement must be in the format 'A AND B' or 'A OR B'")
    
    left_var = tokens[0]
    operator = tokens[1]
    right_var = tokens[2]
    
    if left_var not in values or right_var not in values:
        raise ValueError(f"Variables {left_var} and {right_var} must be in values dict")
    
    left_val = values[left_var]
    right_val = values[right_var]
    
    if operator == "AND":
        return bool(left_val) and bool(right_val)
    elif operator == "OR":
        return bool(left_val) or bool(right_val)
    else:
        raise ValueError(f"Unsupported operator: {operator}")

if __name__ == '__main__':
    result = evaluate_logical_statement('A AND B', {'A': True, 'B': False})
    print(result)