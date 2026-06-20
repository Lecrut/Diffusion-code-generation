def are_equivalent(expr1, expr2):

    def evaluate(expression, assignment):
        return eval(expression, {'__builtins__': None}, assignment)
    variables = set()
    for char in expr1 + expr2:
        if char.isalpha() and char.islower():
            variables.add(char)
    for assignment in product([True, False], repeat=len(variables)):
        assignment_dict = dict(zip(variables, assignment))
        if evaluate(expr1, assignment_dict) != evaluate(expr2, assignment_dict):
            return False
    return True
if __name__ == '__main__':
    print(are_equivalent('a and b', 'b and a'))
    print(are_equivalent('a or b', 'b or a'))
    print(are_equivalent('not a', 'a'))
    print(are_equivalent('a and (b or c)', '(a and b) or (a and c)'))
    print(are_equivalent('a and b', 'a and c'))