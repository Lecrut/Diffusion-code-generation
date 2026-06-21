class BooleanInverter:
    def __init__(self, state: bool) -> None:
        if not isinstance(state, bool):
            raise ValueError("State must be a boolean value")
        self.state = state

    def invert(self) -> bool:
        return not self.state

    def get_state(self) -> bool:
        return self.state

if __name__ == '__main__':
    test_cases = [True, False]
    for case in test_cases:
        inv = BooleanInverter(case)
        print(inv.invert())
        print(inv.get_state())