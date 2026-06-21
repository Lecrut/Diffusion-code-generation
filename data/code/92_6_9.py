class BooleanInverter:
    def __init__(self, initial_state):
        if not isinstance(initial_state, bool):
            raise ValueError("initial_state must be a boolean")
        self._internal_state = initial_state

    def get_opposite(self):
        return not self._internal_state

    def set_state(self, new_state):
        if not isinstance(new_state, bool):
            raise ValueError("new_state must be a boolean")
        self._internal_state = new_state

    def flip(self):
        self._internal_state = not self._internal_state
        return self._internal_state

if __name__ == '__main__':
    inverter = BooleanInverter(True)
    opposite = inverter.get_opposite()
    print(opposite)
    
    inverter.set_state(False)
    opposite = inverter.get_opposite()
    print(opposite)
    
    new_state = inverter.flip()
    print(new_state)
    
    opposite = inverter.get_opposite()
    print(opposite)