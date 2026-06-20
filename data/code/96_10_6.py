class BooleanEvaluator:
    def check_complex_condition(self, states):
        return all(states.get(key) for key in states)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_states = {
        'a': True,
        'b': False,
        'c': True
    }
    print(evaluator.check_complex_condition(sample_states))