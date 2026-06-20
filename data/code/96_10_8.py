class BooleanEvaluator:
    def check_complex_condition(self, states):
        if 'a' not in states or 'b' not in states or 'c' not in states:
            raise ValueError("Dictionary must contain keys 'a', 'b', and 'c'")
        
        a = states['a']
        b = states['b']
        c = states['c']
        
        result = (a and b) or (not c and a)
        return result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_states = {'a': True, 'b': False, 'c': True}
    result = evaluator.check_complex_condition(sample_states)
    print(f"Result: {result}")