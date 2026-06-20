class OppositeTruth:

    def __init__(self, initial_state: bool):
        self.state = initial_state

    def toggle(self) -> bool:
        self.state = not self.state
        return self.state
if __name__ == '__main__':
    ot = OppositeTruth(False)
    print(ot.toggle())