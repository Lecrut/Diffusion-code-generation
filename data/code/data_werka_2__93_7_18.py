class DualBooleanState:
    _FALSE_MAP = {False: 0, True: 1}

    def __init__(self, flag_a: bool, flag_b: bool):
        if not isinstance(flag_a, bool) or not isinstance(flag_b, bool):
            raise ValueError("Attributes must be boolean")
        self.flag_a = flag_a
        self.flag_b = flag_b

    def is_pair_false(self) -> bool:
        combined = self._FALSE_MAP[self.flag_a] + self._FALSE_MAP[self.flag_b]
        return combined == 0

if __name__ == '__main__':
    state = DualBooleanState(False, False)
    print(state.is_pair_false())