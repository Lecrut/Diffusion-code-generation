class BooleanEvaluator:
    def check_complex_condition(self, state_dict):
        if 'a' not in state_dict or 'b' not in state_dict or 'c' not in state_dict:
            raise ValueError("Dictionary must contain keys 'a', 'b', and 'c'")
        
        a = state_dict['a']
        b = state_dict['b']
        c = state_dict['c']
        
        result = (a and not b) or (c and a)
        return result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_state = {'a': True, 'b': False, 'c': True}
    result = evaluator.check_complex_condition(sample_state)
    print(f"Result: {result}")