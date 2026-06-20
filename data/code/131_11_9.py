def evaluate_rules(input_params):
    rules = {
        'A': lambda x: x['a'] > 0,
        'B': lambda x: x['b'] < 10,
        'C': lambda x: x['c'] == True
    }
    
    result = all(rule(input_params) for rule in rules.values())
    return result

if __name__ == '__main__':
    sample_input = {'a': 5, 'b': 3, 'c': True}
    print(evaluate_rules(sample_input))