class BooleanEvaluator:
    @staticmethod
    def evaluate_nested_condition(condition_dict):
        result = condition_dict.get('condition', False)
        if isinstance(result, dict):
            for key, value in result.items():
                if key == 'and':
                    result = all(BooleanEvaluator.evaluate_nested_condition(val) for val in value)
                elif key == 'or':
                    result = any(BooleanEvaluator.evaluate_nested_condition(val) for val in value)
                elif key == 'not':
                    result = not BooleanEvaluator.evaluate_nested_condition(value)
        return result

    def check_complex_condition(self, nested_states):
        return self.evaluate_nested_condition(nested_states)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_conditions = {
        'condition': {
            'and': [
                {'not': True},
                {'or': [False, False]}
            ]
        }
    }
    result = evaluator.check_complex_condition(sample_conditions)
    print(f"Result: {result}")