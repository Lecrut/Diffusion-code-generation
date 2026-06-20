class OppositeTruth:

    def __init__(self, initial_state: bool):
        self.state = initial_state

    def get_opposite(self) -> bool:
        return not self.state
if __name__ == '__main__':
    ot_true = OppositeTruth(True)
    print(ot_true.get_opposite())
    ot_false = OppositeTruth(False)
    print(ot_false.get_opposite())