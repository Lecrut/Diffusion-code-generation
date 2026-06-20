class OppositeTruth:
    def __init__(self, initial_state: bool):
        self.state = initial_state
        self.opposite_map = {True: False, False: True}

    def get_opposite(self) -> bool:
        return self.opposite_map[self.state]

if __name__ == '__main__':
    ot = OppositeTruth(False)
    print(ot.get_opposite())