class RuleBasedMapper:
    def __init__(self, rules):
        self.rules = rules
    def map(self, conditions):
        for rule_id, rule in self.rules.items():
            if self._matches(conditions, rule['conditions']):
                return rule['output']
        return None
    def _matches(self, conditions, required_conditions):
        if not required_conditions:
            return True
        for cond, required_val in required_conditions.items():
            if conditions.get(cond) != required_val:
                return False
        return True
if __name__ == '__main__':
    sample_rules = {
        "Rule_A": {
            "conditions": {"temperature": 30, "humidity": 60},
            "output": "Optimal_Setting_1"
        },
        "Rule_B": {
            "conditions": {"temperature": 20, "humidity": 50},
            "output": "Cool_Setting_2"
        },
        "Rule_C": {
            "conditions": {"temperature": 35},
            "output": "High_Temp_Warning"
        },
        "Rule_D": {
            "conditions": {"humidity": 80},
            "output": "High_Humidity_Alert"
        }
    }
    mapper = RuleBasedMapper(sample_rules)
    test_cases = [
        {"temperature": 30, "humidity": 60},                       
        {"temperature": 20, "humidity": 50},                       
        {"temperature": 35, "humidity": 55},                                                                                           
        {"temperature": 40, "humidity": 80},                       
        {"temperature": 25, "humidity": 55}                      
    ]
    print("--- Rule-Based Mapping Results ---")
    for i, conditions in enumerate(test_cases):
        result = mapper.map(conditions)
        print(f"Test Case {i+1}: Conditions={conditions} -> Output={result}")
    print("---------------------------------")