TRUE_STATE: True
FALSE_STATE: False

class DualBooleanEvaluator:
    def __init__(self, flag_a: bool, flag_b: bool) -> None:
        if not isinstance(flag_a, bool):
            raise ValueError("flag_a must be a boolean")
        if not isinstance(flag_b, bool):
            raise ValueError("flag_b must be a boolean")
        self._val_a = flag_a
        self._val_b = flag_b

    def evaluate_negation_pair(self) -> bool:
        condition_met = self._val_a is FALSE_STATE and self._val_b is FALSE_STATE
        return condition_met

if __name__ == '__main__':
    evaluator = DualBooleanEvaluator(FALSE_STATE, FALSE_STATE)
    outcome = evaluator.evaluate_negation_pair()
    print(outcome)