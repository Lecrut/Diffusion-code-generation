def decide_based_on_input(input_params, decision_rules):
    for rule in decision_rules:
        conditions_met = True
        for key, required_value in rule['conditions'].items():
            if input_params.get(key) != required_value:
                conditions_met = False
                break
        if conditions_met:
            return rule['decision']
    return None
if __name__ == '__main__':
    sample_input = {
        'temperature': 35,
        'humidity': 80,
        'location': 'hot'
    }
    sample_rules = [
        {
            'conditions': {'temperature': 30, 'humidity': 70},
            'decision': 'Mild conditions'
        },
        {
            'conditions': {'temperature': 35},
            'decision': 'Hot weather alert'
        },
        {
            'conditions': {'location': 'hot'},
            'decision': 'Desert heat warning'
        },
        {
            'conditions': {'humidity': 80},
            'decision': 'High humidity advisory'
        }
    ]
    result = decide_based_on_input(sample_input, sample_rules)
    print(result)