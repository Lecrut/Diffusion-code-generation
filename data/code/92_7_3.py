class BooleanFlipper:
    def __init__(self, initial_state: bool):
        self._state = initial_state
    def get_opposite(self) -> bool:
        return not self._state
if __name__ == '__main__':
    flipper1 = BooleanFlipper(True)
    print(f"Initial state of flipper1: {True}")
    print(f"Opposite of flipper1's state: {flipper1.get_opposite()}")
    flipper2 = BooleanFlipper(False)
    print(f"Initial state of flipper2: {False}")
    print(f"Opposite of flipper2's state: {flipper2.get_opposite()}")