def are_equivalent(expr1, expr2):

    def evaluate(expression):
        return eval(expression)
    variables = set()
    for char in expr1 + expr2:
        if char.isalpha() and char not in variables:
            variables.add(char)
    truth_values = [False, True]
    for assignment in product(truth_values, repeat=len(variables)):
        assignments = {var: val for var, val in zip(variables, assignment)}
        expr1_val = evaluate(expr1.format(**assignments))
        expr2_val = evaluate(expr2.format(**assignments))
        if expr1_val != expr2_val:
            return False
    return True
if __name__ == '__main__':
    expr1 = 'A and B'
    expr2 = '(not A) or (not B)'
    print(are_equivalent(expr1, expr2))