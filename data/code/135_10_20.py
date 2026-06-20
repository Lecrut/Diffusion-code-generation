def are_equivalent(statement1: str, statement2: str) -> bool:
    from itertools import product

    def eval_statement(statement: str, values: dict) -> bool:
        exec(f'result = {statement}')
        return result
    variables = set()
    for char in statement1 + statement2:
        if char.isalpha() and char.islower():
            variables.add(char)
    variable_combinations = list(product([True, False], repeat=len(variables)))
    for values in variable_combinations:
        var_dict = dict(zip(variables, values))
        if eval_statement(statement1, var_dict) != eval_statement(statement2, var_dict):
            return False
    return True
if __name__ == '__main__':
    statement1 = 'a and b'
    statement2 = 'b and a'
    print(are_equivalent(statement1, statement2))