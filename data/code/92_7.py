class BooleanFlipper:
    def __init__(self, initial_state: bool):
        self._state = initial_state
    def get_opposite(self) -> bool:
        return not self._state
if __name__ == '__main__':
    state1 = True
    flipper1 = BooleanFlipper(state1)
    result1 = flipper1.get_opposite()
    print(f"Initial state: {state1}, Opposite: {result1}")
    state2 = False
    flipper2 = BooleanFlipper(state2)
    result2 = flipper2.get_opposite()
    print(f"Initial state: {state2}, Opposite: {result2}")