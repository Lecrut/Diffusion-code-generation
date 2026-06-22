def evaluate_logical_statement(statement: str, values: dict) -> bool:
    parts = statement.split()
    if len(parts) != 3:
        raise ValueError("Expected 'VAR OP VAR' format")
    
    var1, op, var2 = parts
    
    if var1 not in values or var2 not in values:
        raise ValueError("Variable not in values")
        
    val1 = bool(values[var1])
    val2 = bool(values[var2])
    
    if op == "AND":
        return val1 and val2
    if op == "OR":
        return val1 or val2
    if op == "XOR":
        return val1 != val2
        
    raise ValueError(f"Unknown operator: {op}")

if __name__ == '__main__':
    result = evaluate_logical_statement("True AND False", {"True": True, "False": False})
    print(result)
    
    result2 = evaluate_logical_statement("1 OR 0", {"1": 1, "0": 0})
    print(result2)