class RuleBasedEngine:
    def __init__(self):
        self.rules = []
    def add_rule(self, condition_func, action):
        if not callable(condition_func) or not callable(action):
            raise TypeError("Condition and Action must be callables.")
        try:
            rule = {"condition": condition_func, "action": action}
            self.rules.append(rule)
        except Exception as e:
            raise RuntimeError(f"Failed to add rule due to {e}")
    def evaluate(self, data):
        if not isinstance(data, dict):
            return None
        decisions = []
        for i, rule in enumerate(self.rules):
            try:
                condition_result = rule["condition"](data)
                if callable(condition_result):
                    result = condition_result()
                else:
                    result = bool(condition_result)
                if not result:
                    continue
                action_func = rule["action"]
                decision = {"rule_index": i, "result": True}
                try:
                    output_data = action_func(data)
                    decision.update({"output": output_data})
                    decisions.append(decision)
                except Exception as e:
                    raise RuntimeError(f"Action failed in rule {i}: {e}")
            except Exception as e:
                raise RuntimeError(f"Condition evaluation error in rule {i}: {e}")
        return decisions if decisions else None
if __name__ == '__main__':
    engine = RuleBasedEngine()
    def check_age(data):
        age = data.get("age")
        try:
            if isinstance(age, (int, float)):
                return True if age >= 18 else False
            raise TypeError(f"Invalid type for 'age', got {type(age).__name__}")
        except Exception as e:
            print(f"Age check error: {e}")
            return None
    def grant_access(data):
        try:
            name = data.get("name")
            if isinstance(name, str) and len(name.strip()) > 0:
                return f"{name} granted access."
            raise ValueError("Name is missing or invalid.")
        except Exception as e:
            print(f"Access grant error: {e}")
            return None
    engine.add_rule(check_age, grant_access)
    sample_data = {"age": 25, "name": "Alice"}
    try:
        result = engine.evaluate(sample_data)
        if isinstance(result, list):
            print("Decisions:")
            for decision in result:
                output_str = str(decision.get("output", "")) or f"Rule {decision['rule_index']} executed but no valid output."
                print(f"  Rule {decision['rule_index']}: {output_str}")
        else:
            print("No decisions made.")
    except Exception as e:
        print(f"Fatal error in evaluation engine: {e}")