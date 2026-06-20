class ShortCircuitEvaluator:
    @staticmethod
    def evaluate_and(a: bool, b: bool) -> bool:
        return a and b

    @staticmethod
    def evaluate_or(a: bool, b: bool) -> bool:
        return a or b

if __name__ == '__main__':
    evaluator = ShortCircuitEvaluator()
    and_result = evaluator.evaluate_and(True, False)
    or_result = evaluator.evaluate_or(False, True)
    print(f'AND Result: {and_result}')
    print(f'OR Result: {or_result}')