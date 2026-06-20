def evaluate_rules(rules, params):
    return all(rule(params) for rule in rules)

if __name__ == '__main__':
    rules = [
        lambda p: p['age'] > 18,
        lambda p: p['income'] >= 50000,
        lambda p: p['education'] == 'bachelor'
    ]
    params = {
        'age': 22,
        'income': 60000,
        'education': 'bachelor'
    }
    print(evaluate_rules(rules, params))