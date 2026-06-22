class StateInverter:
    def __init__(self, is_active: bool):
        if not isinstance(is_active, bool):
            raise ValueError("State must be a boolean")
        self._is_active = is_active
        self._true_val = True
        self._false_val = False
        self._opposite_map = {
            self._true_val: self._false_val,
            self._false_val: self._true_val
        }

    def get_opposite_state(self) -> bool:
        current = self._is_active
        opposite = self._opposite_map[current]
        return opposite

    def set_state(self, new_state: bool) -> None:
        if not isinstance(new_state, bool):
            raise ValueError("State must be a boolean")
        self._is_active = new_state

if __name__ == '__main__':
    inv = StateInverter(False)
    result = inv.get_opposite_state()
    print(result)
    inv.set_state(True)
    result2 = inv.get_opposite_state()
    print(result2)