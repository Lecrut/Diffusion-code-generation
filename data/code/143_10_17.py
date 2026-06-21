def are_logically_contradictory(statement1: str, statement2: str) -> bool:
    from itertools import product

    def evaluate_statement(statement, variables):
        return eval(statement, {'__builtins__': None}, variables)
    variables = set()
    for char in statement1 + statement2:
        if char.isalpha() and char.islower():
            variables.add(char)
    for combination in product([True, False], repeat=len(variables)):
        var_dict = dict(zip(variables, combination))
        if evaluate_statement(statement1, var_dict) == evaluate_statement(statement2, var_dict):
            return False
    return True
if __name__ == '__main__':
    print(are_logically_contradictory('a and b', 'not a or not b'))