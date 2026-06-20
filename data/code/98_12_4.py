def evaluate_complex_logic(variables, conditions):
    for var_name, operator, value in conditions:
        if operator == '==':
            if variables[var_name] != value:
                return False
        elif operator == '<':
            if variables[var_name] >= value:
                return False
        elif operator == '>':
            if variables[var_name] <= value:
                return False
        elif operator == '<=':
            if variables[var_name] > value:
                return False
        elif operator == '>=':
            if variables[var_name] < value:
                return False
    return True

if __name__ == '__main__':
    sample_variables = {'a': 5, 'b': 10}
    sample_conditions = [('a', '==', 5), ('b', '>', 3)]
    print(evaluate_complex_logic(sample_variables, sample_conditions))