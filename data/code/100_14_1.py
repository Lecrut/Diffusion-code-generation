def evaluate_logical_statement(statement, variables):
    if " AND " in statement:
        parts = statement.split(" AND ")
        if len(parts) == 2:
            left_val = variables.get(parts[0].strip())
            right_val = variables.get(parts[1].strip())
            if left_val is not None and right_val is not None:
                return left_val and right_val
    elif " OR " in statement:
        parts = statement.split(" OR ")
        if len(parts) == 2:
            left_val = variables.get(parts[0].strip())
            right_val = variables.get(parts[1].strip())
            if left_val is not None and right_val is not None:
                return left_val or right_val
    elif " NOT " in statement:
        parts = statement.split(" NOT ")
        if len(parts) == 2:
            operand = parts[1].strip()
            if operand in variables:
                return not variables[operand]
    elif statement in variables:
        return variables[statement]
    return False
if __name__ == '__main__':
    variables = {
        'A': True,
        'B': False,
        'C': True
    }
    statement1 = 'A AND B'
    result1 = evaluate_logical_statement(statement1, variables)
    print(f"Statement: {statement1}, Result: {result1}")
    statement2 = 'A OR B'
    result2 = evaluate_logical_statement(statement2, variables)
    print(f"Statement: {statement2}, Result: {result2}")
    statement3 = 'NOT A'
    result3 = evaluate_logical_statement(statement3, variables)
    print(f"Statement: {statement3}, Result: {result3}")
    statement4 = 'C'
    result4 = evaluate_logical_statement(statement4, variables)
    print(f"Statement: {statement4}, Result: {result4}")
    statement5 = 'A AND C'
    result5 = evaluate_logical_statement(statement5, variables)
    print(f"Statement: {statement5}, Result: {result5}")