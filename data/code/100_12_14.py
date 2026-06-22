def parse_logical_statement(statement, **values):
    tokens = statement.split()
    if len(tokens) != 3:
        raise ValueError("Statement must be in format 'VAR1 OP VAR2'")
    
    var1, op, var2 = tokens
    
    if op not in ('AND', 'OR', 'XOR', 'NAND', 'NOR'):
        raise ValueError(f"Unsupported operator: {op}")
    
    val1 = values.get(var1, False)
    val2 = values.get(var2, False)
    
    if op == 'AND':
        return val1 and val2
    elif op == 'OR':
        return val1 or val2
    elif op == 'XOR':
        return val1 ^ val2
    elif op == 'NAND':
        return not (val1 and val2)
    elif op == 'NOR':
        return not (val1 or val2)

if __name__ == '__main__':
    result = parse_logical_statement('A AND B', A=True, B=False)
    print(result)