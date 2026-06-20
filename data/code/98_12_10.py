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
    user_data = {'age': 25, 'membership': True, 'points': 100}
    rules = [('age', '>=', 18), ('membership', '==', True), ('points', '>', 50)]
    is_eligible = evaluate_complex_logic(user_data, rules)
    print("Eligibility Check:", is_eligible)