def are_logically_contradictory(stmt1: str, stmt2: str) -> bool:
    from itertools import product

    def evaluate(statement, var_values):
        for var, val in var_values.items():
            statement = statement.replace(var, str(val).lower())
        return eval(statement)
    vars_set1 = set(stmt1.split()) & {'True', 'False'}
    vars_set2 = set(stmt2.split()) & {'True', 'False'}
    if vars_set1 != vars_set2:
        return False
    var_combinations = list(product([True, False], repeat=len(vars_set1)))
    for combo in var_combinations:
        val1 = evaluate(stmt1, dict(zip(vars_set1, combo)))
        val2 = evaluate(stmt2, dict(zip(vars_set1, combo)))
        if val1 == val2:
            return False
    return True
if __name__ == '__main__':
    stmt1 = 'A and not B'
    stmt2 = 'B or not A'
    print(are_logically_contradictory(stmt1, stmt2))