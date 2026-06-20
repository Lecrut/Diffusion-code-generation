class BooleanEvaluator:
    def check_complex_condition(self, states):
        return (states.get('a', False) and not states.get('b', True)) or (states.get('c', True) and not states.get('d', False))

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_states = {
        'a': True,
        'b': False,
        'c': True,
        'd': False
    }
    result = evaluator.check_complex_condition(sample_states)
    print(f"Result: {result}")