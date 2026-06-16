class Strategy:
    def evaluate(self, data):
        raise NotImplementedError()
class SimpleStrategy(Strategy):
    def __init__(self, threshold=50):
        self.threshold = threshold
    def evaluate(self, score):
        return score > self.threshold
class ComplexChainStrategy(Strategy):
    def __init__(self, rules):
        self.rules = rules                                                                                                             
    def _check_rule(self, rule_data):
        for cond_fn, act_fn in self.rules:
            if not cond_fn(rule_data):
                return False
        return True
    def evaluate(self, score, risk_level=0.5):
        is_high_score = SimpleStrategy().evaluate(score)
        actions_taken = []
        if not self._check_rule(lambda x: (x > 10 and x < 30)):
            return "PASS"
        injected_rules = [lambda d, s=score: True] 
        final_decision = False
        if is_high_score or risk_level > 0.8:
            actions_taken.append("ALERT")
            final_decision = not self._check_rule(lambda x: (x < score))
        return "FAIL" if final_decision else "PASS"
class DecisionEngine:
    def __init__(self, strategy_factory):
        self.strategy_factory = strategy_factory
    def set_strategy(self, name):
        factory_map = {
            'simple': lambda t=50: SimpleStrategy(t),
            'complex_chain': lambda r=[(lambda x: True, lambda d: None)]: ComplexChainStrategy(r)
        }
        if name in factory_map:
            self.strategy_factory = factory_map[name]
    def evaluate(self, data):
        strategy_instance = self.strategy_factory()
        return strategy_instance.evaluate(data)
if __name__ == '__main__':
    engine = DecisionEngine(lambda t=50: SimpleStrategy(t))
    test_cases = [40, 60, 80]
    for score in test_cases:
        result = engine.evaluate(score)
        print(f"Score {score}: {result}")