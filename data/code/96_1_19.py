class BooleanEvaluator:
    def __init__(self):
        self._cache = {}

    def check_complex_condition(self, a: bool, b: bool, c: bool, d: bool) -> bool:
        if not (isinstance(a, bool) and isinstance(b, bool) and isinstance(c, bool) and isinstance(d, bool)):
            raise ValueError("All arguments must be of type bool")
        
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
    val_a = False
    val_b = True
    val_c = True
    val_d = False
    output = evaluator.check_complex_condition(val_a, val_b, val_c, val_d)
    print(output)