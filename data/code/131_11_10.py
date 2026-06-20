def evaluate_rules(params):
    rules = {
        'rule1': params['a'] > 0,
        'rule2': params['b'] < 10,
        'rule3': params['c'] == 'yes'
    }
    return all(rules.values())

if __name__ == '__main__':
    sample_params = {'a': 5, 'b': 7, 'c': 'yes'}
    print(evaluate_rules(sample_params))