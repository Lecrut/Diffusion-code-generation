def evaluate_logical_statement(statement: str, **kwargs) -> bool:
    tokens = statement.upper().split()
    if len(tokens) != 3:
        raise ValueError("Statement must be in the format 'VAR1 OP VAR2'")
    
    var1_name, operator, var2_name = tokens
    
    if operator not in ('AND', 'OR', 'XOR', 'NAND', 'NOR'):
        raise ValueError(f"Unsupported operator: {operator}")
    
    if var1_name not in kwargs:
        raise ValueError(f"Variable {var1_name} not provided")
    if var2_name not in kwargs:
        raise ValueError(f"Variable {var2_name} not provided")
        
    val1 = bool(kwargs[var1_name])
    val2 = bool(kwargs[var2_name])
    
    if operator == 'AND':
        return val1 and val2
    elif operator == 'OR':
        return val1 or val2
    elif operator == 'XOR':
        return val1 ^ val2
    elif operator == 'NAND':
        return not (val1 and val2)
    elif operator == 'NOR':
        return not (val1 or val2)

if __name__ == '__main__':
    result = evaluate_logical_statement('A AND B', A=True, B=False)
    print(result)