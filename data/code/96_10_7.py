class BooleanEvaluator:
    def check_complex_condition(self, states):
        return (states['a'] and not states['b']) or (states['c'] and states['d'])

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