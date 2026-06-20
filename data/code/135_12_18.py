def are_equivalent(expr1, expr2):

    def evaluate(expression):
        return eval(expression)
    variables = set()
    for char in expr1 + expr2:
        if char.isalpha() and char.islower():
            variables.add(char)
    truth_assignments = [dict(zip(variables, assignment)) for assignment in product([True, False], repeat=len(variables))]
    results = []
    for assignment in truth_assignments:
        env = globals().copy()
        env.update(assignment)
        results.append((evaluate(expr1, env), evaluate(expr2, env)))
    return all((result[0] == result[1] for result in results))
if __name__ == '__main__':
    expr1 = 'a and b'
    expr2 = 'b and a'
    print(are_equivalent(expr1, expr2))