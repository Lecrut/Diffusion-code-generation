class OppositeTruth:

    def __init__(self, initial_state=False):
        self.state = initial_state

    def toggle(self):
        self.state = not self.state
        return self.state
if __name__ == '__main__':
    ot = OppositeTruth(True)
    print(ot.toggle())
    print(ot.toggle())