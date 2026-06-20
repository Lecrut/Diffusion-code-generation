class BooleanEvaluator:
    @staticmethod
    def check_complex_condition(nested_dict):
        if isinstance(nested_dict, bool):
            return nested_dict
        elif isinstance(nested_dict, dict) and 'and' in nested_dict:
            return all(BooleanEvaluator.check_complex_condition(val) for val in nested_dict['and'])
        elif isinstance(nested_dict, dict) and 'or' in nested_dict:
            return any(BooleanEvaluator.check_complex_condition(val) for val in nested_dict['or'])
        else:
            raise ValueError("Invalid input format")

if __name__ == '__main__':
    sample_input = {
        'or': [
            {'and': [True, False]},
            {'not': True}
        ]
    }
    result = BooleanEvaluator.check_complex_condition(sample_input)
    print(f"Result: {result}")