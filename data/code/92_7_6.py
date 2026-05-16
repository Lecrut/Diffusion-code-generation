class BooleanFlipper:
    def __init__(self, initial_state: bool):
        self._state = initial_state
    def get_opposite(self) -> bool:
        return not self._state
if __name__ == '__main__':
    flipper1 = BooleanFlipper(True)
    print(f"Initial state of flipper1: {True}")
    opposite1 = flipper1.get_opposite()
    print(f"Opposite of flipper1's state: {opposite1}")
    flipper2 = BooleanFlipper(False)
    print(f"Initial state of flipper2: {False}")
    opposite2 = flipper2.get_opposite()
    print(f"Opposite of flipper2's state: {opposite2}")