class LogicEvaluator:
    def evaluate_logic(self, p, q):
        r = p ^ q
        return (p and q) or (not p and r)

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    test_cases = [(True, True), (True, False), (False, True), (False, False)]
    results = {case: evaluator.evaluate_logic(*case) for case in test_cases}
    print(results)