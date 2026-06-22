class DualBooleanState:
    def __init__(self, first: bool, second: bool) -> None:
        if not isinstance(first, bool):
            raise ValueError("first attribute must be a boolean")
        if not isinstance(second, bool):
            raise ValueError("second attribute must be a boolean")
        self._state1 = first
        self._state2 = second

    def _validate_inputs(self, val1: bool, val2: bool) -> None:
        if not isinstance(val1, bool):
            raise ValueError("Input val1 must be boolean")
        if not isinstance(val2, bool):
            raise ValueError("Input val2 must be boolean")

    def check_false_pair(self, val1: bool, val2: bool) -> bool:
        self._validate_inputs(val1, val2)
        return not val1 and not val2

if __name__ == '__main__':
    state = DualBooleanState(False, False)
    result = state.check_false_pair(False, False)
    print(result)