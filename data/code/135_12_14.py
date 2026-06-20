def are_equivalent(expr1, expr2):

    def evaluate(expr, truth_values):
        return eval(expr, {'__builtins__': None}, truth_values)
    variables = set()
    for char in expr1 + expr2:
        if char.isalpha() and char.islower():
            variables.add(char)
    truth_assignments = [dict(zip(variables, assignment)) for assignment in product([True, False], repeat=len(variables))]
    for assignment in truth_assignments:
        if evaluate(expr1, assignment) != evaluate(expr2, assignment):
            return False
    return True
if __name__ == '__main__':
    expr1 = 'a and b'
    expr2 = 'b and a'
    print(are_equivalent(expr1, expr2))
    expr3 = 'a or b'
    expr4 = 'not (not a and not b)'
    print(are_equivalent(expr3, expr4))
    expr5 = 'a xor b'
    expr6 = '(a and not b) or (not a and b)'
    print(are_equivalent(expr5, expr6))