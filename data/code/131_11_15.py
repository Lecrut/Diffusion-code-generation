def evaluate_rules(input_params):
    rules = {
        'rule1': input_params['a'] > 0,
        'rule2': input_params['b'] < 10,
        'rule3': input_params['c'] == 'yes'
    }
    return all(rules.values())

if __name__ == '__main__':
    sample_input = {'a': 5, 'b': 7, 'c': 'yes'}
    print(evaluate_rules(sample_input))