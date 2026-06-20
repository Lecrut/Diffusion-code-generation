def evaluate_expression(expression: str, variables: dict) -> bool:
    return eval(expression, {"__builtins__": None}, variables)

def generate_truth_table(expressions: list, variables: set):
    truth_values = list(product([True, False], repeat=len(variables)))
    results = []
    for values in truth_values:
        var_dict = dict(zip(variables, values))
        eval_results = [evaluate_expression(expr, var_dict) for expr in expressions]
        results.append(eval_results)
    return results

def are_equivalent(expression1: str, expression2: str):
    variables1 = set(re.findall(r'\b[a-zA-Z]+\b', expression1))
    variables2 = set(re.findall(r'\b[a-zA-Z]+\b', expression2))
    common_variables = variables1.intersection(variables2)
    
    if not common_variables:
        return True
    
    truth_table1 = generate_truth_table([expression1], common_variables)
    truth_table2 = generate_truth_table([expression2], common_variables)
    
    return truth_table1 == truth_table2

if __name__ == '__main__':
    expr1 = "a and b"
    expr2 = "b and a"
    print(are_equivalent(expr1, expr2))