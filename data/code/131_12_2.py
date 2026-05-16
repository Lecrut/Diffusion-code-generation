def decide_based_on_input(input_params, decision_rules):
    for rule in decision_rules:
        match = True
        for condition_key, required_value in rule['condition'].items():
            if input_params.get(condition_key) != required_value:
                match = False
                break
        if match:
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
            'condition': {'temperature': 30, 'humidity': 70},
            'decision': 'Mild conditions'
        },
        {
            'condition': {'temperature': 35},
            'decision': 'Hot weather alert'
        },
        {
            'condition': {'location': 'hot'},
            'decision': 'Desert heat protocol'
        },
        {
            'condition': {'humidity': 80},
            'decision': 'High humidity warning'
        }
    ]
    result = decide_based_on_input(sample_input, sample_rules)
    print(result)