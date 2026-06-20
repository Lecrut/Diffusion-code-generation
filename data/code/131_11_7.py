def evaluate_rules(input_params):
    rules = {
        'rule1': lambda x: x['a'] > 0,
        'rule2': lambda x: x['b'] < 10,
        'rule3': lambda x: x['c'] == True
    }
    
    for rule_name, rule in rules.items():
        if not rule(input_params):
            return False
    
    return True

if __name__ == '__main__':
    sample_input = {'a': 5, 'b': 7, 'c': True}
    print(evaluate_rules(sample_input))