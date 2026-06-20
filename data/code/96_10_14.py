class BooleanEvaluator:
    @staticmethod
    def evaluate_condition(condition_dict):
        if isinstance(condition_dict, dict):
            keys = list(condition_dict.keys())
            if len(keys) == 1:
                key = keys[0]
                value = condition_dict[key]
                if isinstance(value, bool):
                    return value
                elif isinstance(value, dict):
                    return BooleanEvaluator.evaluate_condition(value)
        raise ValueError("Invalid input format")

    def check_complex_condition(self, nested_conditions):
        result = self.evaluate_condition(nested_conditions)
        return result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_conditions = {
        "a": True,
        "b": False,
        "c": True,
        "nested": {
            "d": False,
            "e": (True and not False) or (False and True)
        }
    }
    result = evaluator.check_complex_condition(sample_conditions)
    print(f"Result: {result}")