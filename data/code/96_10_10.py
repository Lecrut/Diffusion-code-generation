class BooleanEvaluator:
    def check_complex_condition(self, state_dict):
        return (state_dict.get('a', False) and not state_dict.get('b', True)) or (state_dict.get('c', False) and state_dict.get('d', False))

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_state = {'a': True, 'b': False, 'c': True, 'd': False}
    result = evaluator.check_complex_condition(sample_state)
    print(f"Result: {result}")