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
        'humidity': 60,
        'location': 'North'
    }
    sample_rules = [
        {
            'condition': {'temperature': 30},
            'decision': 'Mild Weather'
        },
        {
            'condition': {'humidity': 70},
            'decision': 'High Humidity Alert'
        },
        {
            'condition': {'location': 'North', 'temperature': 35},
            'decision': 'Hot and Dry North'
        },
        {
            'condition': {'humidity': 60},
            'decision': 'Moderate Conditions'
        }
    ]
    result = decide_based_on_input(sample_input, sample_rules)
    print(result)