def decide_based_on_input(input_params, rules):
    for rule in rules:
        conditions_met = True
        for key, required_value in rule['conditions'].items():
            if input_params.get(key) != required_value:
                conditions_met = False
                break
        if conditions_met:
            return rule['decision']
    return None
if __name__ == '__main__':
    input_data = {
        "temperature": 35,
        "humidity": 60,
        "location": "North"
    }
    decision_rules = [
        {
            "conditions": {"temperature": 30, "humidity": 50},
            "decision": "Optimal conditions met"
        },
        {
            "conditions": {"temperature": 35},
            "decision": "High temperature warning"
        },
        {
            "conditions": {"location": "North"},
            "decision": "Northern zone alert"
        }
    ]
    result = decide_based_on_input(input_data, decision_rules)
    print(result)