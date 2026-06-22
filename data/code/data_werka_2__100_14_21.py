class LogicEvaluator:
    TRUE_VAL = True
    FALSE_VAL = False

    @staticmethod
    def _compute_r(p, q):
        return p ^ q

    @staticmethod
    def _compute_term1(p, q):
        return p and q

    @staticmethod
    def _compute_term2(p, q):
        r = LogicEvaluator._compute_r(p, q)
        return (not p) and r

    @staticmethod
    def evaluate_logic(p, q):
        term1 = LogicEvaluator._compute_term1(p, q)
        term2 = LogicEvaluator._compute_term2(p, q)
        return term1 or term2

if __name__ == '__main__':
    test_cases = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    results = {}
    for p, q in test_cases:
        results[(p, q)] = LogicEvaluator.evaluate_logic(p, q)
    print(results)