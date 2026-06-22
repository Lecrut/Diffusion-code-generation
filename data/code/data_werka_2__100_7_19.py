class LogicalConditionEvaluator:
    MAX_INT_THRESHOLD = 100
    MIN_STR_LENGTH = 5
    FLOAT_EPSILON = 1e-9

    @staticmethod
    def _validate_inputs(a, b, c, d):
        if not isinstance(a, int):
            raise ValueError("a must be an integer")
        if not isinstance(b, str):
            raise ValueError("b must be a string")
        if not isinstance(c, (int, float)):
            raise ValueError("c must be a number")
        if not isinstance(d, bool):
            raise ValueError("d must be a boolean")

    @staticmethod
    def _compute_primary_metric(a, b):
        if a <= 0:
            return 0
        if len(b) < LogicalConditionEvaluator.MIN_STR_LENGTH:
            return 0
        return a * len(b)

    @staticmethod
    def _compute_secondary_metric(c, d):
        if d:
            return c + 10.0
        return c - 5.0

    @staticmethod
    def _evaluate_logic(primary, secondary, d):
        if primary > LogicalConditionEvaluator.MAX_INT_THRESHOLD:
            if secondary > 50.0:
                return d
            return False
        if secondary < 0.0:
            return not d
        return primary > 10

    def evaluate(self, a, b, c, d):
        self._validate_inputs(a, b, c, d)
        primary_metric = self._compute_primary_metric(a, b)
        secondary_metric = self._compute_secondary_metric(c, d)
        return self._evaluate_logic(primary_metric, secondary_metric, d)

if __name__ == '__main__':
    evaluator = LogicalConditionEvaluator()
    result = evaluator.evaluate(10, "hello", 5.0, True)
    print(result)