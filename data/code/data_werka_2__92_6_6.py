class LogicGate:
    def __init__(self, level: bool):
        self.current_level = level

    def invert(self) -> bool:
        return not self.current_level

    def get_state(self) -> bool:
        return self.current_level

if __name__ == '__main__':
    gate = LogicGate(True)
    opposite_value = gate.invert()
    print(opposite_value)
    
    gate.current_level = False
    print(gate.invert())
    
    initial_state = gate.get_state()
    print(initial_state)