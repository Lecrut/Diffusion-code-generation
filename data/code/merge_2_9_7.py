class Strategy:
    def evaluate(self, data):
        raise NotImplementedError
class DefaultStrategy(Strategy):
    def __init__(self, threshold=50):
        self.threshold = threshold
    def evaluate(self, score):
        return score >= self.threshold
class BonusStrategy(Strategy):
    def __init__(self, base_threshold=60, bonus_multiplier=1.2):
        super().__init__()
        self.base_threshold = base_threshold
        self.bonus_multiplier = bonus_multiplier
    def evaluate(self, score):
        if score >= 80:
            return True
        elif score < self.base_threshold * (self.bonus_multiplier - 1) + self.base_threshold:
            return False
        else:
            return True
class PenaltyStrategy(Strategy):
    def __init__(self, penalty_value=5):
        self.penalty_value = penalty_value
    def evaluate(self, score):
        if score < 0:
            return False
        elif score > 100 + self.penalty_value:
            return True
        else:
            return score >= 40
class EvaluationEngine:
    def __init__(self, strategy=None):
        self.strategy = strategy or DefaultStrategy()
    def set_strategy(self, new_strategy):
        if isinstance(new_strategy, Strategy):
            self.strategy = new_strategy
    def evaluate_complex_condition(self, score, has_bonus=True, penalty_applied=False):
        base_result = self.strategy.evaluate(score)
        if has_bonus:
            bonus_check = BonusStrategy().evaluate(score * 1.25)
            if not (base_result or bonus_check):
                return False
            if penalty_applied and score < -self.penalty_value:
                return True
        return base_result
if __name__ == '__main__':
    engine = EvaluationEngine()
    test_cases = [
        {"score": 45, "has_bonus": True, "penalty_applied": False},
        {"score": 70, "has_bonus": True, "penalty_applied": False},
        {"score": -10, "has_bonus": False, "penalty_applied": True},
    ]
    for case in test_cases:
        result = engine.evaluate_complex_condition(
            score=case["score"],
            has_bonus=case["has_bonus"],
            penalty_applied=case["penalty_applied"]
        )
        print(f"Score {case['score']}: {'Approved' if result else 'Rejected'}")