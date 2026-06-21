import itertools
TRUTH_TABLE = {False: True, True: False}

def evaluate_statement(statement, var_values):
    return eval(statement, {'__builtins__': None}, var_values)

def generate_truth_combinations(variables):
    return list(itertools.product([False, True], repeat=len(variables)))

def check_contradictory_logic(statements):
    variables = set()
    for statement in statements:
        for char in statement:
            if char.isalpha() and char.islower():
                variables.add(char)
    truth_combinations = generate_truth_combinations(variables)
    contradictions = []
    for i, j in itertools.combinations(range(len(statements)), 2):
        stmt1 = statements[i]
        stmt2 = statements[j]
        for var_values in truth_combinations:
            value1 = evaluate_statement(stmt1, dict(zip(variables, var_values)))
            value2 = evaluate_statement(stmt2, dict(zip(variables, var_values)))
            if value1 != value2:
                contradictions.append((i, j))
                break
    return contradictions
if __name__ == '__main__':
    sample_statements = ['A is true', 'B is false', 'A is false', 'B is true', 'A is true']
    contradictory_pairs = check_contradictory_logic(sample_statements)
    print(contradictory_pairs)