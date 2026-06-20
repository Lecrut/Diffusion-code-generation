def evaluate_rules(input_params):
    rules = {
        'rule1': lambda x: x['a'] > 0,
        'rule2': lambda x: x['b'] < 10,
        'rule3': lambda x: x['c'] == True
    }
    return all(rule(input_params) for rule in rules.values())

if __name__ == '__main__':
    sample_params = {'a': 5, 'b': 7, 'c': True}
    print(evaluate_rules(sample_params))