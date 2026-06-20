def evaluate_rules(params):
    rules = {
        'A': lambda x: x > 0,
        'B': lambda x: x < 10,
        'C': lambda x: x % 2 == 0
    }
    
    result = all(rules[key](params[key]) for key in rules if key in params)
    return result

if __name__ == '__main__':
    sample_params = {'A': 5, 'B': 7, 'C': 4}
    print(evaluate_rules(sample_params))