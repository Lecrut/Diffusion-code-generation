class LogicEvaluator:
    OP_AND = "and"
    OP_OR = "or"
    OP_NOT = "not"
    OP_XOR = "^"

    @staticmethod
    def _compute_r(p, q):
        return p ^ q

    @staticmethod
    def _compute_term1(p, q):
        return p and q

    @staticmethod
    def _compute_term2(p, r):
        return (not p) and r

    @staticmethod
    def _combine(term1, term2):
        return term1 or term2

    @staticmethod
    def evaluate_logic(p, q):
        r = LogicEvaluator._compute_r(p, q)
        term1 = LogicEvaluator._compute_term1(p, q)
        term2 = LogicEvaluator._compute_term2(p, r)
        return LogicEvaluator._combine(term1, term2)

if __name__ == '__main__':
    test_cases = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    results = {}
    for p, q in test_cases:
        val = LogicEvaluator.evaluate_logic(p, q)
        results[(p, q)] = val
    print(results)