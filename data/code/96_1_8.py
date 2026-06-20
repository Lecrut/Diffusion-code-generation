class BooleanEvaluator:
    @staticmethod
    def evaluate_nested_logic(a, b, c, d):
        return (a and b) or (c and not d)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.evaluate_nested_logic(True, False, True, False)
    print(result)