class BooleanEvaluator:
    def check_complex_condition(self, a: bool, b: bool, c: bool, d: bool) -> bool:
        return (a and b) or (c and not d)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.check_complex_condition(True, False, True, True)
    print(result)