def evaluate_logical_statement(statement, variables):
    if " AND " in statement:
        parts = statement.split(" AND ")
        if len(parts) == 2:
            left_val = variables.get(parts[0].strip(), False)
            right_val = variables.get(parts[1].strip(), False)
            return left_val and right_val
    elif " OR " in statement:
        parts = statement.split(" OR ")
        if len(parts) == 2:
            left_val = variables.get(parts[0].strip(), False)
            right_val = variables.get(parts[1].strip(), False)
            return left_val or right_val
    elif " NOT " in statement:
        parts = statement.split(" NOT ")
        if len(parts) == 2:
            operand = parts[1].strip()
            if operand in variables:
                return not variables[operand]
    return False
if __name__ == '__main__':
    statement1 = "A AND B"
    variables1 = {"A": True, "B": False}
    result1 = evaluate_logical_statement(statement1, variables1)
    print(f"Statement: {statement1}, Variables: {variables1}, Result: {result1}")
    statement2 = "A OR B"
    variables2 = {"A": True, "B": True}
    result2 = evaluate_logical_statement(statement2, variables2)
    print(f"Statement: {statement2}, Variables: {variables2}, Result: {result2}")
    statement3 = "NOT A"
    variables3 = {"A": True}
    result3 = evaluate_logical_statement(statement3, variables3)
    print(f"Statement: {statement3}, Variables: {variables3}, Result: {result3}")
    statement4 = "B AND NOT A"
    variables4 = {"A": True, "B": False}
    result4 = evaluate_logical_statement(statement4, variables4)
    print(f"Statement: {statement4}, Variables: {variables4}, Result: {result4}")
    statement5 = "A AND B AND C"
    variables5 = {"A": True, "B": True, "C": True}
    result5 = evaluate_logical_statement(statement5, variables5)
    print(f"Statement: {statement5}, Variables: {variables5}, Result: {result5}")