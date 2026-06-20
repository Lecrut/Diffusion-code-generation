def are_equivalent(statement1: str, statement2: str) -> bool:
    from itertools import product
    truth_values = [False, True]
    variables = set(statement1.split()) & set(statement2.split())
    variable_combinations = list(product(truth_values, repeat=len(variables)))
    for combination in variable_combinations:
        env = dict(zip(variables, combination))
        if eval(statement1, env) != eval(statement2, env):
            return False
    return True
if __name__ == '__main__':
    statement1 = 'A and B'
    statement2 = 'B and A'
    print(are_equivalent(statement1, statement2))