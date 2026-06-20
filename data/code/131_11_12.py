input_params = {'age': 30, 'income': 50000, 'has_job': True, 'is_student': False}
rules = [('age >= 18 and income > 20000', True), ('is_student or has_job', True), ('income <= 50000', False)]

def evaluate_rules(params, rules):
    for condition, result in rules:
        if eval(condition, params):
            return result
    return False
if __name__ == '__main__':
    outcome = evaluate_rules(input_params, rules)
    print(outcome)