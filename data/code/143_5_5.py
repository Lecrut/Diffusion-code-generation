import itertools
def evaluate_expression(variables, expression):
    if not expression:
        return False
    sub_expressions = expression.split(' & ')
    if len(sub_expressions) == 1:
        if len(sub_expressions[0]) == 1 and sub_expressions[0] in variables:
            return variables[sub_expressions[0]]
        if sub_expressions[0] == "True":
            return True
        if sub_expressions[0] == "False":
            return False
        return False                                              
    results = [evaluate_expression(variables, expr) for expr in sub_expressions]
    return all(results)
def check_contradiction(constraints, variables):
    if not constraints:
        return False
    var_list = list(variables.keys())
    n = len(var_list)
    for i in range(2**n):
        assignment = {}
        temp_assignment = {}
        for j in range(n):
            temp_assignment[var_list[j]] = bool((i >> j) & 1)
        all_satisfied = True
        for constraint in constraints:
            pass                                          
    return False                                                                                   
def detect_contradiction_simple(constraints, variables):
    var_list = list(variables.keys())
    n = len(var_list)
    for i in range(2**n):
        assignment = {}
        for j in range(n):
            assignment[var_list[j]] = bool((i >> j) & 1)
        all_constraints_met = True
        for constraint in constraints:
            pass 
        pass
    return False
if __name__ == '__main__':
    variables = {'A': True, 'B': False}
    constraints = [
        "A & ~A",                 
        "B"
    ]
    result = True