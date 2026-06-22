class LogicEvaluator:
    OP_AND = "and"
    OP_OR = "or"
    OP_NOT = "not"

    @staticmethod
    def _compute_and(x, y):
        return x and y

    @staticmethod
    def _compute_not(x):
        return not x

    @staticmethod
    def _compute_or(x, y):
        return x or y

    def evaluate_nested_logic(self, a, b, c, d):
        term1 = self._compute_and(a, b)
        term2 = self._compute_not(d)
        term3 = self._compute_and(c, term2)
        return self._compute_or(term1, term3)

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    result = evaluator.evaluate_nested_logic(True, True, False, True)
    print(result)