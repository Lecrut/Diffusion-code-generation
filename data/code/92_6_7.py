class BooleanInverter:
    def __init__(self, state: bool):
        if not isinstance(state, bool):
            raise ValueError("State must be a boolean")
        self._state = state

    def _validate_input(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return value

    def get_opposite(self):
        return not self._state

    def set_state(self, new_state: bool):
        validated = self._validate_input(new_state)
        self._state = validated

if __name__ == '__main__':
    inv = BooleanInverter(True)
    print(inv.get_opposite())
    inv.set_state(False)
    print(inv.get_opposite())
    inv.set_state(True)
    print(inv.get_opposite())