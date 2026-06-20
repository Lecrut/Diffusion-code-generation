class LogicEvaluator:
    @staticmethod
    def evaluate_logic(p: bool, q: bool) -> bool:
        r = p ^ q
        return (p and q) or (not p and r)

if __name__ == '__main__':
    test_cases = [(True, True), (True, False), (False, True), (False, False)]
    results = {case: LogicEvaluator.evaluate_logic(*case) for case in test_cases}
    print(results)