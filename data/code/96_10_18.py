class BooleanEvaluator:
    def check_complex_condition(self, states):
        result = True
        for key, value in states.items():
            if isinstance(value, dict):
                result &= self.check_complex_condition(value)
            elif isinstance(value, bool):
                result &= value
        return result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_states = {
        'a': True,
        'b': {
            'c': False,
            'd': True
        },
        'e': True
    }
    print(evaluator.check_complex_condition(sample_states))