class ConditionEvaluator:
    LABELS = ["positive", "even", "less than 100"]

    @staticmethod
    def _check(condition, label):
        return label if condition else None

    @classmethod
    def combine_checks(cls, is_positive, is_even, is_less_than_100):
        checks = [
            cls._check(is_positive, cls.LABELS[0]),
            cls._check(is_even, cls.LABELS[1]),
            cls._check(is_less_than_100, cls.LABELS[2]),
        ]
        active_checks = [c for c in checks if c is not None]
        
        if not active_checks:
            return "no matches"
        
        return " | ".join(active_checks)

if __name__ == '__main__':
    print(ConditionEvaluator.combine_checks(True, True, True))
    print(ConditionEvaluator.combine_checks(False, False, False))
    print(ConditionEvaluator.combine_checks(True, False, False))