def decide_based_on_input(input_params, decision_rules):
    for rule in decision_rules:
        if check_rule(input_params, rule):
            return rule['decision']
    return None
def check_rule(input_params, rule):
    for key, required_value in rule['conditions'].items():
        if input_params.get(key) != required_value:
            return False
    return True
if __name__ == '__main__':
    sample_input = {
        "temperature": 35,
        "humidity": 60,
        "location": "hot"
    }
    sample_rules = [
        {
            "conditions": {
                "temperature": 30,
                "humidity": 70
            },
            "decision": "High Humidity Alert"
        },
        {
            "conditions": {
                "location": "hot"
            },
            "decision": "Hot Weather Protocol"
        },
        {
            "conditions": {
                "temperature": 35
            },
            "decision": "Moderate Heat Warning"
        }
    ]
    result = decide_based_on_input(sample_input, sample_rules)
    print(result)