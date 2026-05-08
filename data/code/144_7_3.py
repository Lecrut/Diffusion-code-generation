def evaluate_boolean_expression(variables, expression):
    var_map = {var: value for var, value in variables.items()}
    def substitute(expr):
        if expr == 'True':
            return True
        if expr == 'False':
            return False
        return var_map.get(expr, None)
    tokens = expression.split(' & ')
    results = []
    for token in tokens:
        sub_result = substitute(token)
        if sub_result is None:
            raise ValueError(f"Unknown variable or constant: {token}")
        results.append(sub_result)
    return results
def solve_truth_table(variables, expression):
    all_combinations = []
    var_names = sorted(list(variables.keys()))
    n = len(var_names)
    for i in range(2**n):
        current_values = {}
        temp_i = i
        for j in range(n):
            value = bool(temp_i % 2)
            current_values[var_names[j]] = value
            temp_i //= 2
        combination = {var: value for var, value in current_values.items()}
        all_combinations.append(combination)
    results = []
    for combination in all_combinations:
        try:
            result = evaluate_boolean_expression(combination, expression)
            results.append(combination.copy())
        except ValueError as e:
            print(f"Error processing combination: {e}")
    return all_combinations, results
if __name__ == '__main__':
    variables = {
        'P': True,
        'Q': False
    }
    expression = 'P & ~Q'
    combinations, results = solve_truth_table(variables, expression)
    print("Variable Combinations:")
    for combo in combinations:
        print(combo)
    print("\nEvaluation Results:")
    for combo, result in zip(combinations, results):
        print(f"P={combo['P']}, Q={combo['Q']} => Result: {result}")