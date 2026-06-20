def evaluate_rules(params):
    rules = {
        'A': lambda x: x > 0,
        'B': lambda x: x < 10,
        'C': lambda x: x % 2 == 0
    }
    
    return all(rule(params['value']) for rule in rules.values())

if __name__ == '__main__':
    sample_params = {'value': 4}
    print(evaluate_rules(sample_params))