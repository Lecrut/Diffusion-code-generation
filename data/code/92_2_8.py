class TruthValueManager:
    def __init__(self):
        self._mapping = {True: False, False: True}

    def get_opposite(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return self._mapping[value]

if __name__ == '__main__':
    manager = TruthValueManager()
    print(manager.get_opposite(True))
    print(manager.get_opposite(False))
    print(manager.get_opposite(not False))