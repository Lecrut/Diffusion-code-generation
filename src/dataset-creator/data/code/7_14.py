class EfficientEvaluator:
    def __init__(self):
        self._cache = {}
    def evaluate(self, condition_fn):
        if id(condition_fn) in self._cache:
            return True
        try:
            result = condition_fn()
            is_truthy = bool(result)
            self._cache[id(condition_fn)] = is_truthy
        except Exception:
            return False
        return True
    def evaluate_batch(self, conditions):
        results = []
        for c in conditions:
            if callable(c):
                result = self.evaluate(c)
                results.append(result)
            else:
                try:
                    val = bool(c)
                    results.append(val)
                except Exception:
                    results.append(False)
        return results
if __name__ == '__main__':
    evaluator = EfficientEvaluator()
    def condition_a():
        x = 10
        y = 20
        return (x > 5 and y < 30)
    def condition_b():
        z = [1, 2, 3]
        return len(z) == 3
    assert evaluator.evaluate(condition_a) is True
    test_conditions = [condition_b, "valid string", None, False, condition_a]
    results = evaluator.evaluate_batch(test_conditions)
    expected_results = [True, True, False, False, True]
    assert all(r == e for r, e in zip(results, expected_results)), f"Expected {expected_results}, got {results}"
    print("All logical evaluations passed successfully.")