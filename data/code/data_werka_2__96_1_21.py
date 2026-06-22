class BooleanEvaluator:
    OPERATIONS = {'or': lambda x, y: x or y, 'and': lambda x, y: x and y}

    @staticmethod
    def _evaluate_logic(term1: bool, term2: bool) -> bool:
        return BooleanEvaluator.OPERATIONS['or'](term1, term2)

    @staticmethod
    def _evaluate_and_not(term1: bool, term2: bool) -> bool:
        return term1 and (not term2)

    def check_complex_condition(self, a: bool, b: bool, c: bool, d: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool) or not isinstance(d, bool):
            raise ValueError("All inputs must be boolean values")
        
        part1 = a and b
        part2 = BooleanEvaluator._evaluate_and_not(c, d)
        return BooleanEvaluator._evaluate_logic(part1, part2)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.check_complex_condition(False, True, True, False)
    print(result)