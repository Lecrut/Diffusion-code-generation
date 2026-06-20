def are_equivalent(statement1: str, statement2: str) -> bool:
    import itertools

    def eval_statement(statement: str, truth_values: dict) -> bool:
        for var, value in truth_values.items():
            statement = statement.replace(var, str(value).lower())
        return eval(statement)
    variables = set(statement1.split()) | set(statement2.split())
    truth_combinations = list(itertools.product([True, False], repeat=len(variables)))
    for combo in truth_combinations:
        truth_values = dict(zip(variables, combo))
        if eval_statement(statement1, truth_values) != eval_statement(statement2, truth_values):
            return False
    return True
if __name__ == '__main__':
    statement1 = 'p and q'
    statement2 = 'q and p'
    print(are_equivalent(statement1, statement2))