def evaluate_boolean_expression(variables, expression):
    context = {}
    for var_name, var_value in variables.items():
        context[var_name] = var_value
    def substitute(expression_str):
        for var_name, var_value in context.items():
            expression_str = expression_str.replace(var_name, str(var_value))
        return expression_str
    def evaluate_simple_expression(expr):
        if expr == 'True':
            return True
        if expr == 'False':
            return False
        if expr == 'A':
            return context.get('A', False)
        if expr == 'B':
            return context.get('B', False)
        if expr == 'C':
            return context.get('C', False)
        if expr == 'D':
            return context.get('D', False)
        if 'and' in expr:
            parts = expr.split('and')
            return evaluate_simple_expression(parts[0]) and evaluate_simple_expression(parts[1])
        if 'or' in expr:
            parts = expr.split('or')
            return evaluate_simple_expression(parts[0]) or evaluate_simple_expression(parts[1])
        if 'not' in expr:
            parts = expr.split('not')
            return not evaluate_simple_expression(parts[0])
        if expr.startswith('(') and expr.endswith(')'):
            inner = expr[1:-1]
            return evaluate_simple_expression(inner)
        return context.get(expr, False)
    return evaluate_simple_expression(expression)
def solve_truth_table(variables, expression):
    results = []
    variable_names = list(variables.keys())
    n = len(variable_names)
    for i in range(2**n):
        current_values = {}
        temp_i = i
        for j in range(n):
            current_values[variable_names[j]] = bool(temp_i % 2)
            temp_i //= 2
        assignment_str = ""
        for name in variable_names:
            assignment_str += f"{name}={current_values[name]}, "
        assignment_str = assignment_str.rstrip(', ')
        result = evaluate_boolean_expression(current_values, expression)
        results.append((assignment_str, result))
    return results
if __name__ == '__main__':
    variables = {
        'A': True,
        'B': False,
        'C': True,
        'D': False
    }
    expression = "(A and not B) or C"
    truth_table_results = solve_truth_table(variables, expression)
    print("Variable Assignments | Expression Result")
    print("---------------------|-----------------")
    for assignment, result in truth_table_results:
        print(f"{assignment:<20} | {result}")