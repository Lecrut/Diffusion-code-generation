class BooleanState:
    def __init__(self, initial_state: bool):
        self.state = initial_state

    def get_opposite(self) -> bool:
        return not self.state

if __name__ == '__main__':
    sample_value = False
    boolean_state_instance = BooleanState(sample_value)
    opposite_value = boolean_state_instance.get_opposite()
    print(opposite_value)