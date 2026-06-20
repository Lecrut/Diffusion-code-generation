class OppositeTruth:

    def __init__(self, initial_state: bool):
        self.state = initial_state

    def toggle(self) -> bool:
        result = not self.state
        return result
if __name__ == '__main__':
    ot = OppositeTruth(True)
    print(ot.toggle())