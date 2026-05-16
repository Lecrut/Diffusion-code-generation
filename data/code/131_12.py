def decide_based_on_input(input_params, decision_rules):
    for rule in decision_rules:
        condition = rule['condition']
        result = rule['result']
        match = True
        for key, required_value in condition.items():
            if input_params.get(key) != required_value:
                match = False
                break
        if match:
            return result
    return None
if __name__ == '__main__':
    sample_input = {
        'temperature': 35,
        'humidity': 80,
        'location': 'hot'
    }
    sample_rules = [
        {
            'condition': {'temperature': 30, 'humidity': 80},
            'result': 'Action_A'
        },
        {
            'condition': {'location': 'hot'},
            'result': 'Action_B'
        },
        {
            'condition': {'temperature': 40},
            'result': 'Action_C'
        }
    ]
    decision = decide_based_on_input(sample_input, sample_rules)
    print(decision)