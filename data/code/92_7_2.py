class BooleanFlipper:
    def __init__(self, initial_state: bool):
        self._state = initial_state
    def get_opposite(self) -> bool:
        return not self._state
if __name__ == '__main__':
    a = BooleanFlipper(True)
    print(f"Original state: {a._state}")
    print(f"Opposite state: {a.get_opposite()}")
    b = BooleanFlipper(False)
    print(f"Original state: {b._state}")
    print(f"Opposite state: {b.get_opposite()}")