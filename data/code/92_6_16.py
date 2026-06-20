class NotTruth:
    TRUE = True
    FALSE = False

    def __init__(self, initial_state: bool):
        self.state = initial_state

    def get_opposite(self) -> bool:
        return not self.state

if __name__ == '__main__':
    nt = NotTruth(True)
    print(nt.get_opposite())