class TruthManager:
    def __init__(self, value):
        self._value = value
        self._lookup = {True: False, False: True}

    def get_opposite(self):
        return self._lookup[self._value]

if __name__ == '__main__':
    manager = TruthManager(True)
    print(manager.get_opposite())
    manager._value = False
    print(manager.get_opposite())