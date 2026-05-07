class BooleanFlipper:
    def __init__(self, initial_state: bool):
        self._state = initial_state
    def get_opposite(self) -> bool:
        return not self._state
if __name__ == '__main__':
    initial_value = True
    flipper = BooleanFlipper(initial_value)
    opposite_value = flipper.get_opposite()
    print(f"Initial state: {initial_value}")
    print(f"Opposite state: {opposite_value}")
    initial_value = False
    flipper2 = BooleanFlipper(initial_value)
    opposite_value2 = flipper2.get_opposite()
    print(f"Initial state: {initial_value}")
    print(f"Opposite state: {opposite_value2}")