class BooleanEvaluator:
    def __init__(self):
        self._cache = {}

    def check_complex_condition(self, a, b, c, d):
        if not all(isinstance(x, bool) for x in [a, b, c, d]):
            raise ValueError("All arguments must be booleans")
        
        key = (a, b, c, d)
        if key in self._cache:
            return self._cache[key]
        
        first_part = a and b
        second_part = c and (not d)
        final_result = first_part or second_part
        
        self._cache[key] = final_result
        return final_result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    val_a = True
    val_b = True
    val_c = False
    val_d = False
    
    output = evaluator.check_complex_condition(val_a, val_b, val_c, val_d)
    print(output)