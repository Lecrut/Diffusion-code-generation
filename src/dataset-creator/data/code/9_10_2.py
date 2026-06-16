class DecisionEngine:
    def __init__(self):
        self.rules = []
    def add_rule(self, condition_func, action_func):
        if callable(condition_func) and callable(action_func):
            self.rules.append((condition_func, action_func))
        else:
            raise ValueError("Condition and Action must be callable functions.")
    def evaluate(self, data):
        for condition_func, action_func in self.rules:
            try:
                if condition_func(data):
                    return action_func(data)
            except Exception as e:
                continue
        raise ValueError("No applicable rule found.")
def is_above_threshold(value, threshold):
    return isinstance(value, (int, float)) and value > threshold
def apply_action(action_type, data):
    result = f"Executing {action_type} for input: {data}"
    print(result)
    return result
if __name__ == '__main__':
    engine = DecisionEngine()
    def rule_1_condition(data):
        if isinstance(data, dict):
            age = data.get('age', 0)
            salary = data.get('salary', 0.0)
            return (isinstance(age, int) and age >= 30) or (isinstance(salary, float) and salary > 50000)
    def rule_1_action(data):
        if isinstance(data, dict):
            print("Rule 1 Triggered: High Priority Approval")
            return "HIGH_PRIORITY_APPROVAL"
    engine.add_rule(rule_1_condition, rule_1_action)
    def rule_2_condition(value):
        if isinstance(value, (int, float)):
            return value > 50 and value < 75
    def rule_2_action(val):
        print(f"Rule 2 Triggered: Value {val} falls in optimal range.")
        return "OPTIMAL_RANGE"
    engine.add_rule(rule_2_condition, rule_2_action)
    test_data_1 = {'age': 35, 'salary': 60000}
    try:
        result_1 = engine.evaluate(test_data_1)
        print(f"Result for {test_data_1}: {result_1}")
    except ValueError as e:
        print(f"No rule matched for {test_data_1}. Error: {e}")
    test_value = 60
    try:
        result_2 = engine.evaluate(test_value)
        print(f"Result for numeric value {test_value}: {result_2}")
    except ValueError as e:
        print(f"No rule matched for {test_value}. Error: {e}")
    test_data_invalid = "string_input_not_number_or_dict"
    try:
        result_3 = engine.evaluate(test_data_invalid)
        print(f"Result for invalid input: {result_3}")
    except ValueError as e:
        print(f"No rule matched for string. Error: {e}")