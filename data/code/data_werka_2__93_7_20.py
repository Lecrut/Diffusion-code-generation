class DualBooleanEvaluator:
    def __init__(self, first_flag: bool, second_flag: bool):
        self._first = first_flag
        self._second = second_flag

    def are_both_inactive(self) -> bool:
        return not self._first and not self._second

    def get_state_summary(self) -> str:
        if self._first and self._second:
            return "active_active"
        if self._first:
            return "active_inactive"
        if self._second:
            return "inactive_active"
        return "inactive_inactive"

if __name__ == '__main__':
    evaluator = DualBooleanEvaluator(False, False)
    print(evaluator.are_both_inactive())
    print(evaluator.get_state_summary())

    evaluator2 = DualBooleanEvaluator(True, False)
    print(evaluator2.are_both_inactive())
    print(evaluator2.get_state_summary())