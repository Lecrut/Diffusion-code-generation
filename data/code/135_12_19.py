def are_equivalent(expr1, expr2):
    def evaluate(expression, truth_values):
        return eval(expression, {"__builtins__": None}, truth_values)

    variables = set()
    for char in expr1 + expr2:
        if char.isalpha() and char.islower():
            variables.add(char)

    for assignment in product([True, False], repeat=len(variables)):
        truth_dict = dict(zip(variables, assignment))
        if evaluate(expr1, truth_dict) != evaluate(expr2, truth_dict):
            return False
    return True

if __name__ == '__main__':
    print(are_equivalent("(a and b) or (not a)", "b"))