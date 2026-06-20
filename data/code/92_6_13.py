class OppositeTruth:
    def __init__(self, initial_state: bool):
        self.state = initial_state
    
    def get_opposite(self) -> bool:
        return not self.state

if __name__ == '__main__':
    ot = OppositeTruth(True)
    print(ot.get_opposite())
    
    ot.state = False
    print(ot.get_opposite())