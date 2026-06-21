def evaluate_logical_statement(statement: str, values: dict) -> bool:
    tokens = statement.split()
    if len(tokens) != 3:
        raise ValueError("Statement must be in the format 'A AND B' or 'A OR B'")
    
    left_var = tokens[0]
    operator = tokens[1]
    right_var = tokens[2]
    
    if left_var not in values or right_var not in values:
        raise ValueError("Variables not found in values dictionary")
    
    left_val = values[left_var]
    right_val = values[right_var]
    
    if operator == "AND":
        return left_val and right_val
    elif operator == "OR":
        return left_val or right_val
    elif operator == "XOR":
        return left_val ^ right_val
    else:
        raise ValueError(f"Unsupported operator: {operator}")

if __name__ == '__main__':
    result = evaluate_logical_statement("A AND B", {"A": True, "B": False})
    print(result)