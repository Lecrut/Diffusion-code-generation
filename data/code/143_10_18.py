def are_logically_contradictory(statement1: str, statement2: str) -> bool:
    from itertools import product

    def eval_expression(expr: str, vars_dict: dict) -> bool:
        for var, value in vars_dict.items():
            expr = expr.replace(var, str(value).lower())
        return eval(expr)
    variables = set()
    for char in statement1 + statement2:
        if char.isalpha() and char.islower():
            variables.add(char)
    for combination in product([True, False], repeat=len(variables)):
        vars_dict = dict(zip(variables, combination))
        if eval_expression(statement1, vars_dict) == eval_expression(statement2, vars_dict):
            return False
    return True
if __name__ == '__main__':
    print(are_logically_contradictory('a and not b', 'b and not a'))