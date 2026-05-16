def evaluate_expression(variables, expression):
    var_map = {var: val for var, val in variables.items()}
    def substitute(expr):
        if expr == 'True':
            return True
        if expr == 'False':
            return False
        for var, val in var_map.items():
            expr = expr.replace(var, str(val))
        return expr
    substituted_expression = substitute(expression)
    if substituted_expression == 'True':
        return True
    elif substituted_expression == 'False':
        return False
    else:
        raise ValueError(f"Invalid expression result: {substituted_expression}")
def solve_truth_table(variables, expression):
    results = []
    n = len(variables)
    for i in range(2**n):
        current_assignment = {}
        temp_i = i
        for j in range(n):
            current_assignment[variables[j]] = bool(temp_i % 2)
            temp_i //= 2
        results.append(current_assignment)
        substituted_expression = ""
        for var_name, value in current_assignment.items():
            substituted_expression += str(var_name) + " = " + ("True" if value else "False") + " "
        final_result = ""
        for var in variables:
            final_result += f"{var}: {current_assignment[var]}, "
        results.append(final_result.strip())
    return results
if __name__ == '__main__':
    variables = ['P', 'Q']
    def generate_truth_table(vars_list):
        n = len(vars_list)
        table = []
        for i in range(2**n):
            row = {}
            for j in range(n):
                row[vars_list[j]] = bool((i >> j) & 1)
            table.append(row)
        return table
    table_data = generate_truth_table(variables)
    print("Variables:", variables)
    print("---------------------------------")
    print("Truth Table:")
    header = " | ".join(v for v in variables)
    print(f"{'|' + header}")
    for row in table_data:
        row_output = []
        for var in variables:
            row_output.append(str(row[var]))
        print(f"| {' | '.join(row_output)}")