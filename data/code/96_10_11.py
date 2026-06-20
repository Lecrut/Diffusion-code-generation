class BooleanEvaluator:
    def check_complex_condition(self, states):
        if not isinstance(states, dict) or not all(isinstance(k, str) and isinstance(v, bool) for k, v in states.items()):
            raise ValueError("Input must be a dictionary with string keys and boolean values")
        
        result = True
        for key, value in states.items():
            if value:
                result &= self.check_complex_condition(key)
            else:
                result &= not self.check_complex_condition(key)
        
        return result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_states = {
        'A': True,
        'B': False,
        'C': {
            'D': True,
            'E': False
        }
    }
    print(evaluator.check_complex_condition(sample_states))