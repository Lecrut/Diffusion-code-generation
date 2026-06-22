class ZeroEvaluator:
    TRUE_VALUE = True
    FALSE_VALUE = False

    @staticmethod
    def evaluate_zero(x):
        return ZeroEvaluator.TRUE_VALUE if x == 0 else ZeroEvaluator.FALSE_VALUE

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2.5, None, '0', [], {}]
    results = {x: ZeroEvaluator.evaluate_zero(x) for x in sample_values}
    print(results)